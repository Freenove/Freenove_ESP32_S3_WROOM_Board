from machine import Pin,PWM

class myPWM():
    def __init__(self, pwm0: int=15, pwm1: int=2, pwm2: int=0, pwm3: int=4, pwm4: int=5, pwm5: int=18, pwm6: int=19, pwm7: int=21):
        self._pwm0=PWM(Pin(pwm0),10000)
        self._pwm1=PWM(Pin(pwm1),10000)
        self._pwm2=PWM(Pin(pwm2),10000)
        self._pwm3=PWM(Pin(pwm3),10000)
        self._pwm4=PWM(Pin(pwm4),10000)
        self._pwm5=PWM(Pin(pwm5),10000)
        self._pwm6=PWM(Pin(pwm6),10000)
        self._pwm7=PWM(Pin(pwm7),10000)
        
    def ledcWrite(self,chn,value):
        if chn==0:
            self._pwm0.duty(value)
        elif chn==1:
            self._pwm1.duty(value)
        elif chn==2:
            self._pwm2.duty(value)
        elif chn==3:
            self._pwm3.duty(value)
        elif chn==4:
            self._pwm4.duty(value)
        elif chn==5:
            self._pwm5.duty(value)
        elif chn==6:
            self._pwm6.duty(value)
        elif chn==7:
            self._pwm7.duty(value)
    
    def deinit(self):
        self._pwm0.deinit()
        self._pwm1.deinit()
        self._pwm2.deinit()
        self._pwm3.deinit()
        self._pwm4.deinit()
        self._pwm5.deinit()
        self._pwm6.deinit()
        self._pwm7.deinit()
