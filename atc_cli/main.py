import fire
from pathlib import Path

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources
from . import templates

class Contest(object):
    """A simple contest class."""

    def new(self, contest_id, difficulty):
        problem = {
            "contest": contest_id,
            "difficulty": difficulty
        }

        # make contest directory
        contest_dir = Path(contest_id)
        if not contest_dir.exists():
            contest_dir.mkdir(parents=True, exist_ok=True)
        
        # make empty script by difficulty
        problem_file = contest_dir / Path(difficulty + ".py")
        if not problem_file.exists():
            # write template script
            template = pkg_resources.read_text(templates, "solve_problem.py.template")
            populated = template.replace("{{ Problem }}", contest_id + " " + difficulty)
            problem_file.write_text(populated)
        else:
            return "{} already exists.".format(problem_file.name)

        return problem


def contest():
    fire.Fire(Contest)


if __name__ == "__main__":
    contest()