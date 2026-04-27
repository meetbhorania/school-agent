"""School Agent sub-agents package."""

from .english_agent import english_agent
from .maths_agent import maths_agent
from .science_agent import science_agent
from .history_agent import history_agent
from .geography_agent import geography_agent
from .cs_agent import cs_agent

__all__ = [
    "english_agent",
    "maths_agent",
    "science_agent",
    "history_agent",
    "geography_agent",
    "cs_agent",
]
