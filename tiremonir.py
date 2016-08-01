"""Real-time tire-monitoring in iRacing."""
import os
import time

import irsdk


TEMPLATE = r"""
    {: 2d} {: 2d} {: 2d} %            {: 2d} {: 2d} {: 2d} %
     _________               _________
    /         \             /         \
    |         |             |         |
    |         |             |         |
    |         |             |         |
    |         |             |         |
    \_________/             \_________/

    {: 3d} {: 3d} {: 3d} C           {: 3d} {: 3d} {: 3d} C




    {: 2d} {: 2d} {: 2d} %            {: 2d} {: 2d} {: 2d} %
     _________               _________
    /         \             /         \
    |         |             |         |
    |         |             |         |
    |         |             |         |
    |         |             |         |
    \_________/             \_________/

    {: 3d} {: 3d} {: 3d} C           {: 3d} {: 3d} {: 3d} C
"""


def render(text):
    """Update the console."""
    os.system('cls')
    print text


def update(sdk):
    """Return updated data."""
    return (
        22, 4, 99,  # LF %, out->in
        22, 4, 99,  # RF %, in->out

        22, 4, 99,  # LF temps, out->in
        22, 4, 99,  # RF temps, in->out

        22, 4, 99,  # LR %, out->in
        22, 4, 99,  # RR %, in->out

        22, 4, 99,  # LR temps, out->in
        22, 4, 99,  # RR temps, in->out
    )


def run():
    """Tire monitor."""
    ir = irsdk.IRSDK()
    ir.startup()

    while True:
        if True or ir.is_initialized and ir.is_connected:
            values = update(ir)
            ui = TEMPLATE.format(*values)
            render(ui)
        else:
            render('Waiting for iRacing...')
        time.sleep(5)


if __name__ == '__main__':
    run()
