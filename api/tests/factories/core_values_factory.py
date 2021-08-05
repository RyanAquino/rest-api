from factory.alchemy import SQLAlchemyModelFactory
from factory import Sequence
from app import db
from api.models.CoreValue import CoreValue


class CoreValueFactory(SQLAlchemyModelFactory):
    class Meta:
        model = CoreValue
        sqlalchemy_session = db.session

    id = Sequence(lambda n: n+1)
    name = Sequence(lambda n: "CoreValue%s" % n)
