from flask import Flask, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load the duty schedules for all halls
def load_duty_schedules():
    file_path = './data/duty_schedule.xlsx'  # Update with your file path
    sheet_names = ['Campus North', 'Burton Judson', 'I-House', 'Max P', 'RGGRC', 'Snell-Hitchcock', 'Woodlawn']
    schedules = {sheet: pd.read_excel(file_path, sheet_name=sheet) for sheet in sheet_names}
    return schedules

# Get today's duty for each residence hall
def get_today_duty(schedules):
    today = datetime.today().strftime('%Y-%m-%d')  # Get today's date
    today_schedules = {}

    for hall, schedule in schedules.items():
        # Match today's date with schedule's Date column
        schedule['Date'] = pd.to_datetime(schedule['Date']).dt.strftime('%Y-%m-%d')
        today_schedule = schedule[schedule['Date'] == today]
        
        if not today_schedule.empty:
            today_schedules[hall] = today_schedule.iloc[0].to_dict()  # Get today's duty
        else:
            today_schedules[hall] = None  # No one on duty today

    return today_schedules

@app.route('/')
def index():
    schedules = load_duty_schedules()
    today_schedules = get_today_duty(schedules)

    return render_template('index.html', halls=schedules.keys(), today_schedules=today_schedules)

@app.route('/schedule/<hall_name>')
def show_schedule(hall_name):
    schedules = load_duty_schedules()
    today_schedules = get_today_duty(schedules)
    
    if hall_name in schedules:
        schedule = schedules[hall_name]
        today_duty = today_schedules.get(hall_name)  # Get today's duty for this hall
        return render_template('schedule.html', hall_name=hall_name, schedule=schedule.to_dict(orient='records'), today_duty=today_duty)
    else:
        return "Hall not found", 404

if __name__ == '__main__':
    app.run(debug=True)
