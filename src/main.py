import cmd

from data import Run, validate_date, validate_dist, validate_time
from db import add_to_db, query_top5
from plot import scatter_plot_runs


class MyCLI(cmd.Cmd):
    prompt = ">> "
    intro = "Type help for avaiable commands."

    def do_quit(self, line):
        """Exit the CLI."""
        return True

    def do_rrun(self, line):
        """Register a run."""
        try:
            dist = validate_dist(input("Enter distance in kilometers (e.g 5.6): "))
            time = validate_time(input("Enter completion time in format MM:SS : "))
            date = validate_date(
                input("Enter date of completion in format DD/MM/YYYY : ")
            )
            run = Run(dist=dist, time=time, date=date)
            add_to_db(run)

        except ValueError as e:
            print(f"Error: {e}")
            self.do_rrun("")

    def do_top5k(self, line):
        """Lists the 5k's with the fastest completion time."""
        print("5K's with the fastest time: ")
        query_top5(4.9,5.1)

    def do_top10k(self, line):
        """Lists the 10k's with the fastest completion time."""
        query_top5(9.8,10.2)

    def do_plotruns(self, line):
        """Plots runs."""
        """ plottype = input("Enter type of plot: \n • Scatter \n >> ") """
        scatter_plot_runs()
        
"""         match plottype:
            case "scatter" | "Scatter":
                scatter_plot_runs()
            case _:
                print("Invalid plot type")
                self.do_plotruns("")        """ 
        
        


if __name__ == "__main__":
    MyCLI().cmdloop()
