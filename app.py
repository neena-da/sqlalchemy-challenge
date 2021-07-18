import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Index Route
@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"Temperature statistics from given date(yyyy-mm-dd): /api/v1.0/start<br/>"
        f"Temperature statistics between two given dates(yyyy-mm-dd): /api/v1.0/start/end"
    )

# Precipitaion API route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date one year from the last date in data set amd run a query to obtain date and precipitaion for last 12 months
    one_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_date).all()

    session.close()

    precipitaion ={}
    for date_prcp, prcp in results:
        precipitaion[date_prcp] = prcp

    return jsonify(precipitaion)

# Station API route
@app.route("/api/v1.0/stations")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Run a query to get all the station ids
    station_results = session.query(Station.station).all()

    session.close()

    all_stations = list(np.ravel(station_results))
    return jsonify(all_stations)

# Temperature API route
@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date one year from the last date in data set.
    one_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Finding the most active station id and running query to obtain the temperature for the last 12 months in the most active station
    most_active_station = session.query(Measurement.station).\
                                group_by(Measurement.station).\
                                order_by(func.count(Measurement.station).desc()).first()

    tobs_results = session.query(Measurement.date, Measurement.tobs).\
                    filter(Measurement.date >= one_year_date).\
                    filter(Measurement.station == most_active_station[0]).all()

    session.close()

    all_tobs = []
    for dt_tobs, prcp_tobs in tobs_results:
        all_tobs.append(prcp_tobs)
    return jsonify(all_tobs)

# Start/End Date API route

@app.route("/api/v1.0/<start>")

def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    input_date_fmt = dt.datetime.strptime(start, "%Y-%m-%d")
    start_date = input_date_fmt.strftime("%Y-%m-%d")

    end_date = dt.date(2017, 8, 23).strftime("%Y-%m-%d")      # Latest date in the dataset

    # This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
    # and return the minimum, maximum, and average temperatures for that range of dates
    def calc_temps(start_date, end_date):
        return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    stat_results = calc_temps(start_date, end_date)[0]

    session.close()

    stat_list = list(np.ravel(stat_results))
    stat_dict = {'Temps': stat_list}

    return jsonify(stat_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    input_date_fmt = dt.datetime.strptime(start, "%Y-%m-%d")
    start_date = input_date_fmt.strftime("%Y-%m-%d")

    end_date_fmt = dt.datetime.strptime(end, "%Y-%m-%d")
    end_date = end_date_fmt.strftime("%Y-%m-%d")

    # This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
    # and return the minimum, maximum, and average temperatures for that range of dates
    def calc_temps(start_date, end_date):
        return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    stat_results = calc_temps(start_date, end_date)[0]

    session.close()

    stat_list = list(np.ravel(stat_results))
    stat_dict = {'Temps': stat_list}

    return jsonify(stat_dict)
      

if __name__ == '__main__':
    app.run(debug=True)
