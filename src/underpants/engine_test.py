from __future__ import annotations

from pants.engine.rules import QueryRule, rule

from underpants.engine import TestRulesEngine


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
