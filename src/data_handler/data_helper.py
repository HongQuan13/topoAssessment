from datetime import datetime


class DataHelper:
    @staticmethod
    def format_data(data):
        try:
            float_format = data
            if isinstance(data, str):
                float_format = data.replace(",", "")

            return round(float(float_format), 2)
        except (ValueError, TypeError):
            try:
                return int(data)
            except (ValueError, TypeError):
                return str(data) if data else "N/A"

    @staticmethod
    def format_date(date_str, date_format="%d-%m-%Y"):
        if date_str is None or date_str.lower() == "unknown":
            return "N/A"

        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        return date_obj.strftime(date_format)
