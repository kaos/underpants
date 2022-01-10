from __future__ import annotations

from dataclasses import dataclass

from pants.engine.rules import Get, QueryRule, _uncacheable_rule, collect_rules, rule
from pants.util.logging import LogLevel


@dataclass(frozen=True)
class SimpleResult:
    answer: int


@dataclass(frozen=True)
class InputData:
    text: str


@dataclass(frozen=True)
class OutputData:
    text: str


_state = dict(value=40)


@_uncacheable_rule(level=LogLevel.INFO)
# @rule
async def answer_to_life_universe_and_everything() -> SimpleResult:
    data = await Get(OutputData, InputData("answer"))
    # This prints each time, as it is not cached between scheduler sessions.
    print("== data:", data)

    _state["value"] += 1
    return SimpleResult(_state["value"])


# @_uncacheable_rule()
@rule(level=LogLevel.INFO)
async def reverse_input(request: InputData) -> OutputData:
    # This prints only once as it is cached between scheduler sessions.
    print("== in reverse_input:", request)
    return OutputData("".join(reversed(request.text)))


@dataclass(frozen=True)
class Proc:
    cmd: str


@dataclass(frozen=True)
class FallibleProcResult:
    code: int


@dataclass(frozen=True)
class ProcResult:
    code: int
    err: str | None = None


@dataclass(frozen=True)
class ProcCmd:
    value: str


@rule
async def proc_cmd(proc: Proc) -> ProcCmd:
    return ProcCmd(proc.cmd)


@rule
async def exec_proc(proc: Proc) -> FallibleProcResult:
    return FallibleProcResult(0 if proc.cmd == "cmd" else 1)


@rule
async def proc_result(res: FallibleProcResult, cmd: ProcCmd) -> ProcResult:
    # This shows how input params (i.e. `Proc` here) may be shared between rules, as long as they
    # are on the same "level" in the graph.
    if res.code == 0:
        return ProcResult(0)
    return ProcResult(res.code, f"proc {cmd.value!r} failed")


def rules():
    return [
        *collect_rules(),
        # Each "top-level" type that we should be able to request from the engine must have a
        # corresponding `QueryRule` registered, declaring the rule's required input params.
        QueryRule(SimpleResult, ()),
        QueryRule(ProcResult, (Proc,)),
    ]
