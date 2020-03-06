import fire
from pathlib import Path

class Contest(object):
    """A simple contest class."""

    def start(self, contest_id, difficulty):
        problem = {
            "contest": contest_id,
            "difficulty": difficulty
        }

        # make contest directory
        contest_dir = Path(contest_id)
        if not contest_dir.exists():
            contest_dir.mkdir()
        
        # make empty script by difficulty
        problem_file = contest_dir / Path(difficulty + ".py")
        if not problem_file.exists():
            problem_file.touch()
        return problem


def contest():
    fire.Fire(Contest)


if __name__ == "__main__":
    start()