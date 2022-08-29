import pyvisa as visa


class DeviceM:
    instrument_is_open = False

    def __init__(self, cfg_file: str):
        with open(cfg_file) as f:
            self.instrument_idn = f.read().strip()

        self.instrument = str()
        self.idn = 'Error'

        self.rm = visa.ResourceManager("@py")
        self.rm.list_resources()

        if self.open_instrument() != 'Ok':
            self.idn = 'Error'
        else:
            self.get_idn()

        self.close_instrument()

    def get_idn(self):

        if self.open_instrument() != 'Ok':
            return 'Error'

        try:
            self.idn = self.instrument.query("*IDN?")
        except visa.VisaIOError as e:
            print(e.args)
            return 'Error'

        return self.idn

    def open_instrument(self):
        if not self.instrument_is_open:
            try:
                self.instrument = self.rm.open_resource(self.instrument_idn)
                self.instrument_is_open = True
                return 'Ok'
            except visa.VisaIOError as e:
                print(e.args)
                self.close_instrument()
                return 'Error'
        else:
            return 'Ok'

    def close_instrument(self):
        self.instrument.close()
        self.instrument_is_open = False

    def make_meas(self):

        if self.open_instrument() != 'Ok':
            return 'Error'

        try:
            self.instrument.write("ROUT:SCAN (@101:110);:TRIG:SOUR BUS;COUN 1;:INIT;")
        except visa.VisaIOError as e:
            print(e.args)
            return 'Error'

        try:
            self.instrument.write("*TRG")
        except visa.VisaIOError as e:
            print(e.args)
            return 'Error'

        data = 'Error'

        try:
            data = self.instrument.query("FETC?")
        except visa.VisaIOError as e:
            print(e.args)
            return 'Error'

        print(data.encode())
        return data
