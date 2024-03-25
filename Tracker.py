class Tracked_Values:
    comp_count = 0
    write_count = 0
    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_comp():
        return Tracked_Values.comp_count

    @staticmethod
    def reset():
        Tracked_Values.comp_count = 0

    def __str__(self):
        return str(self.value)

    #비교 연산자가 실행될 때 비교 연산뿐만 아니라 count도 1 증가시키도록 변화
    def trace_comp(comp):
        def wrapper(*args, **kwargs):
            Tracked_Values.comp_count += 1
            return comp(*args, **kwargs)
        return wrapper
    
    @trace_comp
    def __lt__(self, other):
        return self.value < other.value
    
    @trace_comp
    def __le__(self, other):
        return self.value <= other.value
    
    @trace_comp
    def __eq__(self, other):
        return self.value == other.value
    
    @trace_comp
    def __ne__(self, other):
        return self.value != other.value

    @trace_comp
    def __gt__(self, other):
        return self.value > other.value
    
    @trace_comp
    def __ge__(self, other):
        return self.value >= other.value
    