from factory.alchemy import SQLAlchemyModelFactory
from factory import Sequence
from app import db
from api.models.Principle import Principle


class PrincipleFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Principle
        sqlalchemy_session = db.session

    id = Sequence(lambda n: n+1)
    name = Sequence(lambda n: "Principle%s" % n)
