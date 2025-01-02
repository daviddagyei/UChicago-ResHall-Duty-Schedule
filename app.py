from flask import Flask, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load the duty schedules for all halls
def load_duty_schedules():
    file_path = './data/duty_schedule.xlsx'  # file path
    sheet_names = ['Campus North', 'Burton Judson', 'I-House', 'Max P', 'RGGRC', 'Snell-Hitchcock', 'Woodlawn']

    # Get actual sheet names in the file
    available_sheets = pd.ExcelFile(file_path).sheet_names

    # Load schedules for available sheets only
    schedules = {sheet: pd.read_excel(file_path, sheet_name=sheet) for sheet in sheet_names if sheet in available_sheets}
    
    return schedules

# Function to get today's duty for each hall (with primary and secondary duty)
def get_today_duty(schedules):
    today = datetime.today().strftime('%Y-%m-%d')  # Get today's date
    today_primary_schedules = {}
    today_secondary_schedules = {}

    for hall, schedule in schedules.items():
        schedule['Date'] = pd.to_datetime(schedule['Date']).dt.strftime('%Y-%m-%d')
        today_schedule = schedule[schedule['Date'] == today]

        if not today_schedule.empty:
            today_primary_schedules[hall] = today_schedule.iloc[0].to_dict()  # Get primary duty
            today_secondary_schedules[hall] = today_schedule.iloc[0].to_dict()  # Get secondary duty
        else:
            # If no schedule is found, leave it blank
            today_primary_schedules[hall] = None
            today_secondary_schedules[hall] = None

    return today_primary_schedules, today_secondary_schedules

@app.route('/')
def index():
    schedules = load_duty_schedules()
    today_primary_schedules, today_secondary_schedules = get_today_duty(schedules)
    hall_images = {
        'Campus North': 'images/campus_north.jpg',
        'Burton Judson': 'images/burton_judson.jpg',
        'I-House': 'images/i_house.jpg',
        'Max P': 'images/max_p.jpg',
        'RGGRC': 'images/rgg_rc.jpg',
        'Snell-Hitchcock': 'images/snell_hitchcock.jpg',
        'Woodlawn': 'images/woodlawn.jpg'
    }
    return render_template('index.html', halls=schedules.keys(), today_primary_schedules=today_primary_schedules, today_secondary_schedules=today_secondary_schedules, hall_images=hall_images)

@app.route('/schedule/<hall_name>')
def show_schedule(hall_name):
    schedules = load_duty_schedules()

    if hall_name in schedules:
        schedule = schedules[hall_name]  # Get full schedule for the hall
        today_primary_schedules, today_secondary_schedules = get_today_duty(schedules)
        today_duty = today_primary_schedules.get(hall_name)  # Get today's duty for this hall
        return render_template('schedule.html', hall_name=hall_name, schedule=schedule.to_dict(orient='records'), today_duty=today_duty)
    else:
        return render_template('schedule.html', hall_name=hall_name, schedule=[], today_duty=None)

if __name__ == '__main__':
    app.run(debug=True)
