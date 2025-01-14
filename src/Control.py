import machine
import time
class Control :

    def __init__(self):
    
      self.entrada = None
      self.salida = None
      self.señal = False
      self.last_sign = True
  
    def assign_in(self, pin_number) :
      self.entrada = machine.Pin(pin_number, machine.Pin.IN)

    def assign_out(self, pin_number):
      self.salida = machine.Pin(pin_number, machine.Pin.OUT)

    def confirm_sign(self):
      self.señal = self.entrada.value()
      time.sleep_ms(50)
      return self.señal

    def close_sign(self):
      self.señal = False
      print('End of service')
      self.salida.off()
      time.sleep_ms(50)

    def check_stock(self, boolean) :
      print('Existing of stock !')
      time.sleep_ms(50)
      return boolean

    def deliver(self):
      print('Deliver product')
      time.sleep_ms(50)
      self.close_sign()

    def loop(self):
      while True:
        while (self.last_sign != self.confirm_sign()) :
          self.last_sign = self.confirm_sign()
          print('Request accepted')
          time.sleep_ms(50)
          self.salida.on()
          if(self.check_stock(True)) :
            self.deliver()
          
