from api.models.CoreValue import CoreValue
from api.models.Principle import Principle
from api.db import db
from api.api import app


CoreValues = [
    "Individuals and Interactions Over Processes and Tools",
    "Working Software Over Comprehensive Documentation",
    "Customer Collaboration Over Contract Negotiation",
    "Responding to Change Over Following a Plan",
]

Principles = [
    "Customer satisfaction through early and continuous software delivery",
    "Accommodate changing requirements throughout the development process",
    "Frequent delivery of working software",
    "Collaboration between the business stakeholders and developers throughout the project",
    "Support, trust, and motivate the people involved",
    "Enable face-to-face interactions",
    "Working software is the primary measure of progress",
    "Agile processes to support a consistent development pace",
    "Attention to technical detail and design enhances agility",
    "Simplicity",
    "Self-organizing teams encourage great architectures, requirements, and designs",
    "Regular reflections on how to become more effective",
]

with app.app_context():
    for i in CoreValues:
        core_value = CoreValue(id=None,name=i)
        db.session.add(core_value)
        db.session.commit()

    for i in Principles:
        principle = Principle(id=None,name=i)
        db.session.add(principle)
        db.session.commit()
