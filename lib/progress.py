"""
lib/progress.py

by BBaoVanC

This library allows easy generation of progress bars.
"""


# Progress bar generator
def genbar(length=20, progress=0, max=100):
    """Generates a progress bar.

    The design of the progress bar:
    Progress: [#####---------------] 25%"""
    percent = round(progress/max, 2)  # percentage has two decimal places
    barsfilled = int(round(length*percent, 0))  # calculate bars filled
    barsunfilled = int(length-barsfilled)  # calculate bars not filled
    progbar = "[{}{}]".format("#"*barsfilled, "-"*barsunfilled)  # make bar
    return "{} {}%".format(progbar, int(percent*100))  # return output
