from time import sleep

import click

from pants_rules.engine import RulesEngine
from pr.demo.basic import Proc, ProcResult, SimpleResult


@click.command()
def main():
    engine = RulesEngine.create(
        "demo",
        backends=("pr.demo",),
        args=(
            # "--level=trace",
            "--no-local-cache",
            "--local-store-dir=.pants.d/basic/lmdb_store",
            "--named-caches-dir=.pants.d/basic/named_caches",
        ),
    )
    with engine.pants_logging():
        for x in range(2):
            with engine.new_session(f"demo-{x % 3}") as session:
                result = session.request(SimpleResult)
                print(f"The result is: {result}")
            sleep(0.5)

        for x in range(2):
            with engine.new_session(f"proc-{x % 3}") as session:
                result = session.request(ProcResult, Proc("cmd" if not x % 2 else "fail"))
                print(f"The result is: {result}")
            sleep(0.5)


if __name__ == "__main__":
    main()
