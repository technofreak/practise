"""Chess Game Handler

This module is influenced by Jeff Ullman's example of a Chess game to teach
finite automata.

input: a string containing a series of characters of S or O, S meaning the
Servicer and O meaning the Opponent. Each character stands for who scored a
point in a particular service. The sequence should finally lead to a win.

result: S for one who is serving to be the winner, O for the opponent to be 
the winner.
"""

class NoInput(Exception):
	pass

class InadequateSequence(Exception):
	pass

class SequenceTooLong(Exception):
	pass

SWIN = {'verbose': 'Server Win',  'nexts': None, 'nexto': None}
OWIN = {'verbose': 'Opponent Win',  'nexts': None, 'nexto': None}
DEUCE2 = {'verbose': '',  'nexts': None, 'nexto': None}
ADVOUT = {'verbose': 'Adv Opp',  'nexts': DEUCE2, 'nexto': OWIN}
ADVIN = {'verbose': 'Adv Server',  'nexts': SWIN, 'nexto': DEUCE2}
DEUCE = {'verbose': 'Deuce',  'nexts': ADVIN, 'nexto': ADVOUT}
FRTYTRTY = {'verbose': '40-30',  'nexts': SWIN, 'nexto': DEUCE}
TRTYFRTY = {'verbose': '30-40',  'nexts': DEUCE, 'nexto': OWIN}
FRTYFFTN = {'verbose': '40-15',  'nexts': SWIN, 'nexto': FRTYTRTY}
FFTNFRTY = {'verbose': '15-40',  'nexts': TRTYFRTY, 'nexto': OWIN}
TRTYALL = {'verbose': '30-All',  'nexts': FRTYTRTY, 'nexto': TRTYFRTY}
FFTNTRTY = {'verbose': '15-30',  'nexts': TRTYALL, 'nexto': FFTNFRTY}
TRTYFFTN = {'verbose': '30-15',  'nexts': FRTYFFTN, 'nexto': TRTYALL}
LOVEFRTY = {'verbose': '0-40',  'nexts': FFTNTRTY, 'nexto': OWIN}
FRTYLOVE = {'verbose': '40-0',  'nexts': SWIN, 'nexto': FRTYFFTN}
LOVETRTY = {'verbose': '0-30',  'nexts': FFTNTRTY, 'nexto': LOVEFRTY}
TRTYLOVE = {'verbose': '30-0',  'nexts': FRTYLOVE, 'nexto': TRTYFFTN}
FFTNALL = {'verbose': '15-All',  'nexts': TRTYFFTN, 'nexto': FFTNTRTY}
LOVEFFTN = {'verbose': '0-15',  'nexts': FFTNALL, 'nexto': LOVETRTY}
FFTNLOVE = {'verbose': '15-0',  'nexts': TRTYLOVE, 'nexto': FFTNALL}
LOVE = {'verbose': 'Service Start',  'nexts': FFTNLOVE, 'nexto': LOVEFFTN}


class Game(object):
	def __init__(self, seq=None):
		if not seq:
			raise NoInput
		self.seq = seq
		self.winner = None
		self.state = LOVE

	def _getNext(self, char):
		if char == 'S':
			next = self.state['nexts']
		else:
			next = self.state['nexto']
		if next == DEUCE2:
			next = DEUCE
		return next

	def result(self):
		for char in seq:
			if self.state == SWIN or self.state == OWIN:
				raise SequenceTooLong
			next = self._getNext(char)
			self.state = next
			#print self.state['verbose'], ">>", char, ">>", next['verbose']
			continue
		if self.state == SWIN:
		    self.winner = 'Server'
		elif self.state == OWIN:
		    self.winner = 'Opponent'
		else:
			raise InadequateSequence
		return self.winner

if __name__ == "__main__":
	seq = 'SOSOSOSOOO'
	game = Game(seq)
	print "Winner of", seq, "is", game.result()
