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
        
        # populate script template by difficulty
        problem_file = contest_dir / Path(difficulty + ".py")
        if not problem_file.exists():
            # read script template from package resources
            SOLVE_PROBLEM_TEMPLATE = "solve_problem.py.template"
            try:
                template = pkg_resources.read_text(templates, SOLVE_PROBLEM_TEMPLATE)
            except Exception as e:
                print("{}: error with reading template file in package resouces.".format(type(e)))
                print("clean up temporaly files...")
                contest_dir.rmdir()
                return "has cleaned up"

            # write script template by problem info
            populated = template.replace("{{ Problem }}", contest_id + " " + difficulty)
            try:
                problem_file.write_text(populated)
            except Exception as e:
                print("{}: error with writing script template".format(type(e)))
                print("clean up temporaly files...")
                contest_dir.rmdir()
                return "has cleaned up"

        else:
            return "{} already exists.".format(problem_file.name)

        return problem


def contest():
    fire.Fire(Contest)


if __name__ == "__main__":
    contest()