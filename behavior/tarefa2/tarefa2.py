from transitions import Machine

class estudante(object):

    states = ['estudando', 'no bar', 'descansando']

    def __init__(self, name):
        self.name = name
        self.machine = Machine(model=self, states=estudante.states, initial='descansando')
        self.machine.add_transition(trigger='prova_no_dia_seguinte', source='*', dest = 'estudando')
        self.machine.add_transition(trigger='passou_a_prova', source='estudando', dest = 'no bar')
        self.machine.add_transition(trigger='bebado', source='no bar', dest = 'descansando')


student = estudante(name='Arthur')

# Triggering the transitions
student.prova_no_dia_seguinte()
print(f"{student.name} is now in state: {student.state}")

student.passou_a_prova()
print(f"{student.name} is now in state: {student.state}")

student.bebado()
print(f"{student.name} is now in state: {student.state}")