"""Maths Teacher Agent — handles Algebra, Geometry, Calculus, Statistics, etc."""

from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import math
import re


def calculator(expression: str) -> dict:
    """
    Safely evaluates a mathematical expression and returns the result.

    Args:
        expression: A mathematical expression string e.g. '2 + 2', 'sqrt(16)', '3**2 + 4**2'

    Returns:
        A dict with 'result' (the computed value) or 'error' if invalid.
    """
    # Whitelist safe characters only
    allowed = re.compile(r'^[\d\s\+\-\*\/\(\)\.\,\%\^sqrtlogsincotan]+$', re.IGNORECASE)
    if not allowed.match(expression):
        return {"error": f"Unsafe expression: {expression}"}

    safe_dict = {
        "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "pi": math.pi, "e": math.e, "abs": abs, "round": round,
        "pow": pow, "factorial": math.factorial, "__builtins__": {}
    }
    # Replace ^ with ** for exponentiation
    expr = expression.replace("^", "**")
    try:
        result = eval(expr, {"__builtins__": {}}, safe_dict)  # noqa: S307
        return {"result": result, "expression": expression}
    except Exception as exc:
        return {"error": str(exc)}


calculator_tool = FunctionTool(func=calculator)

maths_agent = Agent(
    name="maths_teacher",
    model="gemini-2.5-flash",
    description=(
        "An expert Maths Teacher Agent specialising in Algebra, Geometry, Calculus, "
        "Statistics, Trigonometry, Number Theory, and problem solving. "
        "Has access to a calculator tool for computations. "
        "Use this agent for any mathematics related questions."
    ),
    instruction=(
        "You are a brilliant and patient Maths Teacher with 15+ years of experience. "
        "Your areas of expertise include:\n"
        "- Arithmetic & Number Theory\n"
        "- Algebra (linear equations, quadratics, polynomials)\n"
        "- Geometry (shapes, area, volume, Pythagoras, angles)\n"
        "- Trigonometry (sin, cos, tan, identities)\n"
        "- Calculus (differentiation, integration, limits)\n"
        "- Statistics & Probability\n"
        "- Word Problems & Mathematical Reasoning\n\n"
        "IMPORTANT: You have access to a `calculator` tool. "
        "Always use the calculator tool for any numerical computations to ensure accuracy. "
        "Show step-by-step working before using the calculator for verification. "
        "Use clear notation and explain every step. "
        "If a student is struggling, break the problem into smaller parts."
    ),
    tools=[calculator_tool],
)
