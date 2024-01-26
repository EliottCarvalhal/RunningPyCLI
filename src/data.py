from dataclasses import dataclass
import re


@dataclass
class Run:
    dist: int
    time: int
    date: str
    _id: int = None


def calculate_pace(dist, time):
    try:
        minutes, seconds = map(int, time.split(':'))
        total_minutes = minutes + seconds / 60
        pace = total_minutes / dist
        pace_minutes = int(pace)
        pace_seconds = int((pace - pace_minutes) * 60)
        return f"{pace_minutes:02d}:{pace_seconds:02d}"
    except (ValueError, ZeroDivisionError):
        return None

def validate_dist(dist):
    try:
        dist = float(dist)
        if dist >= 0:
            return dist
        else:
            raise ValueError("Distnace is negative.")
    except ValueError:
        raise ValueError("Invalid distance format.")


def validate_time(time):
    time_pattern = re.compile(r"^\d{2}:\d{2}$")
    if time_pattern.match(time):
        return time
    else:
        raise ValueError("Invalid time format.")


def validate_date(date):
    date_pattern = re.compile(r"^\d{2}/\d{2}/\d{4}$")
    if date_pattern.match(date):
        return date
    else:
        raise ValueError("Invalid date format.")
