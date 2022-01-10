from __future__ import annotations

import os
import sys
from contextlib import contextmanager
from dataclasses import dataclass, replace
from typing import Any, Iterable, Iterator, TypeVar, cast

from pants.build_graph.build_configuration import BuildConfiguration
from pants.engine.environment import CompleteEnvironment
from pants.engine.internals.scheduler import SchedulerSession
from pants.engine.internals.selectors import Params
from pants.engine.internals.session import SessionValues
from pants.init.engine_initializer import EngineInitializer
from pants.init.extension_loader import load_backend
from pants.init.logging import initialize_stdio, stdio_destination
from pants.option.global_options import DynamicRemoteOptions
from pants.option.option_value_container import OptionValueContainer
from pants.option.options_bootstrapper import OptionsBootstrapper
from pants.testutil.option_util import create_options_bootstrapper
from pants.util.collections import assert_single_element

_O = TypeVar("_O")


@dataclass(frozen=True)
class RulesEngine:
    build_config: BuildConfiguration
    global_options: OptionValueContainer
    session: SchedulerSession

    @classmethod
    def create(
        cls,
        id: str,
        *,
        backends: Iterable[str] = (),
        args: Iterable[str] = (),
    ) -> RulesEngine:
        build_config = cls.create_build_config(backends)
        environment = CompleteEnvironment(os.environ)
        options_bootstrapper = create_options_bootstrapper(args=args)
        options = options_bootstrapper.full_options(build_config)
        global_options = options_bootstrapper.bootstrap_options.for_global_scope()
        dynamic_remote_options, _ = DynamicRemoteOptions.from_options(options, environment)

        graph_session = EngineInitializer.setup_graph(
            bootstrap_options=global_options,
            build_configuration=build_config,
            dynamic_remote_options=dynamic_remote_options,
        ).new_session(
            build_id=id,
            session_values=SessionValues(
                {
                    OptionsBootstrapper: options_bootstrapper,
                    CompleteEnvironment: environment,
                }
            ),
        )

        return cls(
            build_config=build_config,
            global_options=global_options,
            session=graph_session.scheduler_session,
        )

    @staticmethod
    def create_build_configuration_builder() -> BuildConfiguration.Builder:
        return BuildConfiguration.Builder()

    @classmethod
    def create_build_config(cls, backends: Iterable[str]) -> BuildConfiguration:
        build_config_builder = cls.create_build_configuration_builder()
        for backend in backends:
            load_backend(build_config_builder, backend)

        return build_config_builder.create()

    def request(self, output_type: type[_O], *inputs: Any) -> _O:
        result = assert_single_element(self.session.product_request(output_type, [Params(*inputs)]))
        return cast(_O, result)

    @contextmanager
    def pants_logging(self):
        stdin_fileno = sys.stdin.fileno()
        stdout_fileno = sys.stdout.fileno()
        stderr_fileno = sys.stderr.fileno()
        with initialize_stdio(self.global_options), stdio_destination(
            stdin_fileno=stdin_fileno,
            stdout_fileno=stdout_fileno,
            stderr_fileno=stderr_fileno,
        ):
            yield

    @contextmanager
    def new_session(self, id: str) -> Iterator[RulesEngine]:
        yield replace(self, session=self.session.scheduler.new_session(id))
