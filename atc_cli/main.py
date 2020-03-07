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

    def new(self, contest_id, level):

        problem = {
            "contest": contest_id,
            "level": level
        }

        # make contest directory
        contest_dir = Path(contest_id)
        if not contest_dir.exists():
            contest_dir.mkdir(parents=True, exist_ok=True)
        
        # populate script template by level
        problem_file = contest_dir / Path(level + ".py")
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
            populated = template.replace("{{ Problem }}", contest_id + " " + level)
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
    
    def clean(self, contest_id, level="", all=False):
        problem = {
            "contest": contest_id,
            "level": level
        }

        # check contest directory exists
        contest_dir = Path(contest_id)
        if not contest_dir.exists():
            return "{} does not exist.".format(contest_dir.name)
        
        # check all option
        if all:
            for p in contest_dir.iterdir():
                if p.is_file():
                    p.unlink()
            return "has cleaned up."

        # check problem script exists
        if level == "":
            return "without --all option, required specified level"
        problem_file = contest_dir / Path(level + ".py")
        if not problem_file.exists():
            return "{} does not exist.".format(problem_file.name)
        
        # clean up
        try:
            problem_file.unlink()
        except Exception as e:
            return e

        return "has cleaned up"






def contest():
    fire.Fire(Contest)


if __name__ == "__main__":
    contest()