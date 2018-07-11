# python functions for binomial web analytics
# from scipy import stats as st
import math

def binom_sd(phat, a, b):
	#math.sqrt((0.5 * 0.5)/(15348 + 15312))
	return math.sqrt((phat * (1-phat)) / (a + b))
	
def binom_me(sd, z):
	# sd * 1.96 (zscore)
	return sd*z
	
def binom_cnfint(me,cnt):
	#print ("confIntvl: %f ---- $f ---- %f" % ((me-cnt),cnt,(me+cnt)))	
	# ll = me - cnt, mid = cnt, up = me + cnt
	return (cnt-me), cnt, (me+cnt)

def binom_phat(a, b):
	return (a / (a + b))
	
def binom_stsig(phat, me, cnt):
	# verify the phat is in the confidence interval
	if (phat >= (cnt -me)) and (phat <= (cnt+me)):
		return True
	else:
		return False
		
def binom_check(p, a, b, zscore):
	# call calculated phat - probability
	sd = binom_sd(p, a, b)
	me = binom_me(sd, zscore)
	cphat = binom_phat(a, b)
	ci = binom_cnfint(me, p)
	ssig =  binom_stsig(cphat, me, p)
	
	print ('calc-sd:   %f' % (sd))
	print ('calc-me:   %f' % (me))
	print ('calc-phat: %f' % (cphat))
	print ('calc-ci:   min: %f -- cnt: %f -- max: %f' % (ci))
	print ('stsig: 	   %r' % (ssig))
	
	