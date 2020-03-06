import fire
from pathlib import Path

class Contest(object):
    """A simple contest class."""

    def start(self, contest_id, difficulty):
        problem = {
            "contest": contest_id,
            "difficulty": difficulty
        }
        contest_dir = Path(contest_id)
        print(contest_dir.exists())
        if not contest_dir.exists():
            contest_dir.mkdir()
        print(contest_dir.exists())
        return problem


def contest():
    fire.Fire(Contest)


if __name__ == "__main__":
    start()