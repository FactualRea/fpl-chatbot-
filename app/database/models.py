from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    fpl_id = Column(Integer, unique=True, nullable=False)
    first_name = Column(String)
    second_name = Column(String)
    web_name = Column(String)
    team = Column(String)
    position = Column(String)

    gameweeks = relationship("PlayerGameweek", back_populates="player")


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True)
    season_name = Column(String, unique=True, nullable=False)


class PlayerGameweek(Base):
    __tablename__ = "player_gameweeks"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    season = Column(String)
    gameweek = Column(Integer)
    minutes = Column(Integer)
    goals = Column(Integer)
    assists = Column(Integer)
    bonus = Column(Integer)
    bps = Column(Integer)
    points = Column(Integer)
    xg = Column(Float)
    xa = Column(Float)
    price = Column(Float)
    ownership = Column(Float)

    player = relationship("Player", back_populates="gameweeks")


class Fixture(Base):
    __tablename__ = "fixtures"

    id = Column(Integer, primary_key=True)
    season = Column(String)
    gameweek = Column(Integer)
    home_team = Column(String)
    away_team = Column(String)
    difficulty = Column(Integer)
    finished = Column(Boolean, default=False)