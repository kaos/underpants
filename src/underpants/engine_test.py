from __future__ import annotations

from typing import Callable, Iterable, Union, cast

from pants.build_graph.build_configuration import BuildConfiguration
from pants.engine.rules import QueryRule, Rule, rule
from pants.engine.unions import UnionRule

from underpants.engine import RulesEngine


class TestRulesEngine(RulesEngine):
    test_rules: tuple[Rule, ...] = ()

    @classmethod
    def create_with_rules(
        cls, *rules: Union[Rule, Callable, UnionRule], id: str = "test", args: Iterable[str] = ()
    ) -> RulesEngine:
        class WithRules(TestRulesEngine):
            # The pants.engine.RuleIndex class accepts callables with a `rule` attribute.
            test_rules = cast("tuple[Rule, ...]", tuple(rules))

        return WithRules.create(id)

    @classmethod
    def create_build_configuration_builder(cls) -> BuildConfiguration.Builder:
        builder = super().create_build_configuration_builder()
        builder.register_rules(cls.__name__, cls.test_rules)
        return builder


class Answer(int):
    pass


class FormatString(str):
    pass


class Formatted(str):
    pass


def test_simple_rule() -> None:
    @rule
    async def the_answer() -> Answer:
        return Answer(42)

    @rule
    async def format_answer(fmt: FormatString, answer: Answer) -> Formatted:
        return Formatted(fmt.format(answer=answer))

    engine = TestRulesEngine.create_with_rules(
        the_answer,
        format_answer,
        QueryRule(Formatted, (FormatString,)),
    )
    assert engine.request(Formatted, FormatString("The answer is {answer}.")) == "The answer is 42."
