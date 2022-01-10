"""CSC111 Winter 2022: Welcome File

To run this file, right-click anywhere in the text and select "Run File in Python Console".
(This should appear as an option after you've imported the PyCharm settings found in
csc111_pycharm_settings.zip.)
"""
# Check that you can import every library in requirements.txt
import pytest
import python_ta
import plotly.graph_objects as go
import pygame

from hypothesis import given
from hypothesis.strategies import integers


def test_pygame() -> None:
    """Check if pygame can be initialized."""
    num_pass, num_fail = pygame.init()

    assert num_pass > 0, "None of pygame's imported modules could be initialized"
    assert num_fail == 0, "At least one of pygame's imported modules could not be initialized"


@given(x=integers())
def test_hypothesis(x: int) -> None:
    """Check if hypothesis is working."""
    assert isinstance(x, int)


def try_plotly() -> None:
    """Check if you can generate a plot with plotly."""
    # Convert the outputs into parallel x and y lists
    x_data, y_data = [1, 2, 3], [10, 8, 12]

    # Create the figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data))

    # Configure the figure
    fig.update_layout(title='A Scatter Plot',
                      xaxis_title='An x-axis',
                      yaxis_title='A y-axis')

    # Show the figure in the browser
    fig.show()
    # Is the above not working for you? Comment it out, and uncomment the following:
    # fig.write_html('my_figure.html')
    # You will need to manually open the my_figure.html file created above.


if __name__ == '__main__':
    python_ta.check_all(config={
        'extra-imports': ['plotly.graph_objects', 'pygame', 'hypothesis.strategies'],
        'max-line-length': 100,
        'disable': ['E1101']
    })

    try_plotly()

    pytest.main(['welcome.py'])
