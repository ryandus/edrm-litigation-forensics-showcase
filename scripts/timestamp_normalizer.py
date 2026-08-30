"""
timestamp_normalizer.py
Standardizes disparate timestamps (Local offset, GPS epoch, drifting DVR clocks) into unified UTC ISO-8601.
"""

from datetime import datetime, timedelta, timezone

def normalize_events(input_records):
    normalized = []
    
    for record in input_records:
        raw_time = record['raw_timestamp']
        source = record['source_type']
        offset_hours = record.get('timezone_offset_hours', 0)
        dvr_drift_seconds = record.get('dvr_drift_seconds', 0)
        
        dt = datetime.strptime(raw_time, "%Y-%m-%d %H:%M:%S")
        dt_utc = dt - timedelta(hours=offset_hours)
        
        if dvr_drift_seconds != 0:
            dt_utc = dt_utc - timedelta(seconds=dvr_drift_seconds)
            
        dt_utc = dt_utc.replace(tzinfo=timezone.utc)
        
        normalized.append({
            'Event_ID': record['event_id'],
            'Source': source,
            'DateTime_UTC': dt_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
            'Description': record['description']
        })
        
    normalized.sort(key=lambda x: x['DateTime_UTC'])
    return normalized

if __name__ == "__main__":
    sample_data = [
        {'event_id': 'EV01', 'source_type': 'ALPR', 'raw_timestamp': '2026-08-10 07:12:00', 'timezone_offset_hours': -7, 'dvr_drift_seconds': 0, 'description': 'FLOCK ALPR camera hit'},
        {'event_id': 'EV02', 'source_type': 'CCTV', 'raw_timestamp': '2026-08-10 07:52:30', 'timezone_offset_hours': -7, 'dvr_drift_seconds': 300, 'description': 'Commercial DVR capture (drifting +5m)'},
        {'event_id': 'EV03', 'source_type': 'CSLI', 'raw_timestamp': '2026-08-10 14:45:00', 'timezone_offset_hours': 0, 'dvr_drift_seconds': 0, 'description': 'Carrier CDR tower dwell start'}
    ]
    
    results = normalize_events(sample_data)
    print("Chronologically Normalized Multi-Source Timeline:")
    for r in results:
        print(f"[{r['DateTime_UTC']}] ({r['Source']}) {r['Description']}")