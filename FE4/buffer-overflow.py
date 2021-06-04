vals = [None]*10
for i in range(0, 20):
    vals[i] = i


# anatomy of a memory

##########
## KERNEL ## think of this as your command line, this sits at the 'top'
## STACK ## this is what matters during a buffer overflow attack
## HEAP ##
## DATA ##
## TEXT ## think of this as your read-only code, like a bunch of zeros, this sits at the 'bottom'
##########

# anatomy of the stack using a sample register

##########
## ESP (Extended Stack Pointer) ##
## Buffer Space ## send a bunch of characters like "AAAAAAA" and the buffer space should ideally contain these characters that we are sending
## EBP (Extended Base Pointer) ## but if we have a buffer overflow attack we will reach here
## EIP (Extended Instruction Pointer) / Return Address ## and here -- we can send instructions or malicious code that can access a server's shell
##########
