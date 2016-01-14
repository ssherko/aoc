BSHELL=`which bash`
BSCRIPT=run.sh
STORE?=0

runlast:
	@$(BSHELL) $(BSCRIPT) last

runall:
	@$(BSHELL) $(BSCRIPT) all $(STORE)
	

new:
	@$(BSHELL) $(BSCRIPT) new_day

clean:
	@rm *.pyc