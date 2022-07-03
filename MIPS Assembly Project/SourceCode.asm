.data
	#Global Strings
	newLine_text: .asciiz "\n"
	input_message: .asciiz "Input: "
	
	#Menu Strings
	welcome_message: .asciiz "Welcome to our MIPS project!"
	menu_message: .asciiz "\nMain Menu:\n1. Base Converter\n2. Add Rational Number\n3. Text Parser\n4. Mystery Matrix Operation\n5. Exit\nPlease select an option: "
	exit_message: .asciiz "\nProgram ends. Bye :)\n"
	invalidInput_message: .asciiz "\nPlease enter a valid option.\n"

	#Question1 Strings	
	type_message: .asciiz "Type: "
	binaryInput_Q1: .space 16
	forNegation: .asciiz "-"

	#Question2 Strings
	numerator1: .asciiz "Enter the first numerator: "
	denominator1: .asciiz "Enter the first denominator: "
	numerator2: .asciiz "Enter the second numerator: "
	denominator2: .asciiz "Enter the second denominator: "
	slash: .asciiz "/"
	plus: .asciiz "+"
	equals: .asciiz "="
	output_text: .asciiz "Output:\n"
	
	#Question3 Strings
	inputText_message: .asciiz "\nInput Text: "
	InputText_Q3: .space 200
	parserCharacters_message: .asciiz "Parser Characters: "
	parsers_input: .space 10
	
	#Question4 String
	wecouldnt_message: .asciiz "We couldn't :("
	
	
.text
  main:
    li $v0, 4
    la $a0, welcome_message
    syscall

	while:
		#Prints the menu
		li $v0, 4
		la $a0, menu_message
		syscall
		
		#Getting input from user
		li $v0, 5
		syscall
		move $t0, $v0
	
		#cases
		case_1: bne $t0, 1, case_2
			jal question1		
			j while
        
        	case_2: bne $t0, 2, case_3
			jal question2		
			j while
        
        	case_3: bne $t0, 3, case_4
			jal question3		
			j while
		
		case_4: bne $t0, 4, case_5
			jal question4    				
    			j while
        
        	case_5: bne $t0, 5, invalidInput
			beq $t0, 5, exit

        	invalidInput: #check whether the input is valid or not
			li $v0, 4
			la $a0, invalidInput_message
			syscall
			j while

		exit:
			li $v0, 4           
			la $a0, exit_message
			syscall		#prints bye
		
			li $v0, 10
			syscall     #ending program

question1:
	li $v0, 4
    	la $a0, input_message
    	syscall
    	
    	li $v0, 8
    	la $a0, binaryInput_Q1
    	li $a1, 16
    	syscall    
    	move $t0, $a0
    	
    	li $v0, 4
    	la $a0, type_message
    	syscall	
    	
    	li $v0, 5
    	syscall
    	
    	addi $t1, $zero, 1
    	addi $t8, $zero, 2
    	
    	beq $v0, $t1, type1SolutionQ1 #checking type input
    	
    	beq $v0, $t8, type2SolutionQ1
    	
    type1SolutionQ1:
    	addi $t5, $zero, 0 # initialize the count to 0
	lb $t1, 0($t0)
	addi $t2, $t1, -48
	seq $t4, $t2, 1

	#here is to calculate length			
loop:
	lb $t1, 0($t0) # load the next character into t1
	seq $t3, $t1, 10
	bnez $t3, binaryToDecimal # check for the null character
	addi $t0, $t0, 1 # increment the string pointer
	addi $sp, $sp, -1
	sb $t1, 0($sp)
	addi $t5, $t5, 1 # increment the count
	j loop 

#At the end of this loop, the length value will be in $t5 register

binaryToDecimal:
	move $t3, $t5   #Not to lose real length value, we move it to $t3 register to make processes
	addi $t6, $zero, 0  
	beqz $t4, pos  #checks the first bit. If 0, go pos label else goes neg

neg:
	lb $t1, 0($sp)     #gets from stack
	addi $t2, $t1, -48 #substract from 48 and gets whether it is 0 or 1
	bnez $t2, calc     #If 1, goes calc label and calculate
	addi $sp, $sp, 1
	addi $t3, $t3, -1
	j neg

calc:
	sub $t7, $t5, $t3    #calculates the step where we are according the real length value - $t3 to make processes
	addi $t8, $zero, 1
	sllv $t8, $t8, $t7  #2^$t7. For example at first length=8, temp length=8. 8-8=0. We'll use it to multiply it with sum
	add $t6, $t6, $t8   # sum
	j negloop
	
negloop:
	addi $sp, $sp, 1
	addi $t3, $t3, -1
	beqz $t3, negation
	lb $t1, 0($sp)
	addi $t2, $t1, -48
	beqz $t2, calc
	j negloop

negation:
	addi $t7, $zero, -1
	mult $t6, $t7
	li $v0, 4
	la $a0, forNegation
	syscall
	
	j out

pos:
	lb $t1, 0($sp)
	addi $t2, $t1, -48
	bnez $t2, calc2
	j posloop

calc2:
	sub $t7, $t5, $t3
	addi $t8, $zero, 1  #calculates for positive binary
	sllv $t8, $t8, $t7
	add $t6, $t6, $t8
	j posloop
	
posloop:
	addi $sp, $sp, 1
	addi $t3, $t3, -1
	beqz $t3, out
	lb $t1, 0($sp)
	addi $t2, $t1, -48
	bnez $t2, calc2
	j posloop

out:
	li $v0, 1
	move $a0, $t6
	syscall

 j while   #in the end, return back to menu
    	
    type2SolutionQ1:
    		addi $t5, $zero, 0 # length 0 in the beginning
    		addi $s0, $zero, 0
	loopQ2:
		lb $t1, 0($t0)
		seq $t3, $t1, 10
		bnez $t3, binaryToDecimalQ2 
		addi $t0, $t0, 1 
		addi $t5, $t5, 1
		j loopQ2 #return back loopQ2 label
    		    	
    	
    	binaryToDecimalQ2:
    		addi $t4, $zero,-1 #Using for grouping 4 bits
    		addi $t6, $zero, 0 #sum
    	
    	whileLoopQ2:  #main while loop
    	    beqz $t5, outQ2
    	    addi $t4, $t4,1
    	    beq $t4, 4, hexCalc
    	    addi $t5, $t5,-1
    	    addi $t0, $t0, -1
    	    lb $t1, 0($t0)
    	    addi $t2, $t1, -48
 	    bnez $t2, calcQ2
 	    j whileLoopQ2

	calcQ2:
		addi $t7, $zero, 1
		sllv $t7, $t7, $t4
		add $t6, $t6, $t7
		j whileLoopQ2
    		
    	hexCalc:
    		addi $sp, $sp, -1
    		addi $s0, $s0, 1   
    		bge $t6, 10, hexValforLetters  #checks the number if it is less than 10, add it to 48 to get ascii, else goes hexValforLetters label
    		addi $t6, $t6, 48
    	store:
    		sb $t6, 0($sp)     #store to the stack
    		j binaryToDecimalQ2
    		
    	hexValforLetters:
    		addi $t6, $t6, 55    #here is for numbers that thair result is greater than 10. Add 55 to get ascii between A-F
    		j store	
    		
    	outQ2:
    		bne $t4, -1, hexCalc
    		beqz $s0, exit2
    		lb $t6, 0($sp)
    		li $v0, 11
    		move $a0, $t6
		syscall
    		addi $sp, $sp, 1
    		addi $s0, $s0, -1
    		j outQ2
    	
    	exit2:
    		j while   	
    	
    	

question2:
	li $v0, 4
    	la $a0, numerator1    #Prints the message "Enter the first numerator: "
    	syscall
    	
    	li $v0, 5
    	syscall            #Gets the first numerator from user
    	move $t0, $v0      #Save the first numerator value to the $t0 register
    	
    	li $v0, 4
    	la $a0, denominator1  #Prints the message "Enter the first denominator: "
    	syscall
    	
    	li $v0, 5
    	syscall            #Gets the first denominator from user
    	move $t1, $v0	   #Save the first denominator value to the $t1 register
    	
    	li $v0, 4
    	la $a0, numerator2    #Prints the message "Enter the second numerator: "
    	syscall
    	
    	li $v0, 5
    	syscall            #Gets the second numerator from user
    	move $t2, $v0      #Save the second numerator value to the $t2 register
    	
    	li $v0, 4
    	la $a0, denominator2  #Prints the message "Enter the second denominator: "
    	syscall
    	
    	li $v0, 5
    	syscall            #Gets the second denominator from user
    	move $t3, $v0	   #Save the second denominator value to the $t3 register
    	
    	mul $t4, $t0, $t3  #numerator1 * denominator2
    	mul $t5, $t1, $t2  #numerator2 * denominator1
    	add $t6, $t4, $t5  #(numerator1*denominator2 + numerator2*denominator1)
    	mul $t7, $t1, $t3  #denominator1 * denominator2
    	
    	
    	li $v0, 4
    	la $a0, output_text  #Prints "Output:"
    	syscall
    	
    	li $v0, 1
    	move $a0, $t0   #Prints First numerator
    	syscall
    	
    	li $v0, 4
    	la $a0, slash  #To represent rational numbers, prints "/"
    	syscall
    	
    	li $v0, 1
    	move $a0, $t1  # Prints first denominator
    	syscall
    	
    	
    	li $v0, 4
    	la $a0, plus   #To represent addition of rational numbers, prints "+"
    	syscall
    	
    	li $v0, 1
    	move $a0, $t2  # Prints second numerator
    	syscall
    	
    	li $v0, 4
    	la $a0, slash  #Again, To represent rational numbers, prints "/"
    	syscall
    	
    	li $v0, 1
    	move $a0, $t3  # Prints second denominator
    	syscall
    	
  	li $v0, 4
    	la $a0, equals #Prints "=" 
    	syscall
    	
    	addi $t0, $zero, 1 #Counter
    	addi $s2, $zero, 0 #GCD Value
   forLoopGCD: #main while loop for Q2
    	
    	#First we'll check whether counter is less than or equal to first number and also less than or equal to second number
    	
    	
    	sle $t1, $t0, $t6   #To continue the loop, checks if counter $t0<=$t6. $t6 is (numerator1*denominator2 + numerator2*denominator1)
    	sle $t2, $t0, $t7   # checks second one. $t0<=$t7. $t7 is denominator1 * denominator2 here.
    	and $t3, $t1, $t2   # we used "and" operator here because we need both of them to be True.
    	beqz $t3, calcCanonicalForm  #if not, it means that loop is over and assuming that we found GCD of them. Go to calculate
    	
    	
    	#If condition of $t3 is True, then we need to find their GCD. After that, we are calculating it with loop
    	div $t6, $t0  
    	mfhi $s1  #Remainder
    	sle $t4, $s1, $zero 
    	
    	div $t6, $t0
    	mfhi $s1 #Remainder
    	sle $t5, $s1, $zero
    	
    	and $t3, $t4, $t5
    	beqz $t3,incrementAndReturnLoop 
    	move $s2, $t0
    	j incrementAndReturnLoop
    	
    	incrementAndReturnLoop:
    		addi $t0, $t0, 1
    		j forLoopGCD
    		
    	#The logic here is that if we found GCD value of two numbers, we need to divide both of them to GCD value. This is 
    	#what we used here to find canonical form for Question2.	
    	calcCanonicalForm:  
    		div $t1, $t6, $s2
    		div $t2, $t7, $s2
    		
    		li $v0, 1
    		move $a0, $t1
    		syscall
    	        beq $t2, 1, returnMainLoop
    		li $v0, 4
    		la $a0, slash
    		syscall
    	
    		li $v0, 1
    		move $a0, $t2
    		syscall
    	
    	   returnMainLoop:
    	      j while
    	
	
question3:
	li $v0, 4
    	la $a0, input_message #Prints "Input: "
    	syscall
    	
    	li $v0, 4
    	la $a0, inputText_message #Prints "Input Text: "
    	syscall
    	
    	li $v0, 8
    	la $a0, InputText_Q3   #Gets the input text from the user
    	li $a1, 200
    	syscall    
    	move $s0, $a0
    	
    	li $v0, 4
    	la $a0, parserCharacters_message #Prints the message "Parser Characters: "
    	syscall
    	
    	li $v0, 8
    	la $a0, parsers_input    #Gets parser characters from the user
    	li $a1, 10
    	syscall    
    	
    	move $s1, $a0
    	
    	move $t0, $s0
    	move $t1, $s1
    	
    	addi $t2, $zero, 0   #Sub string count. 
    	
    	mainLoopQ3:
    	   lb $t3, 0($t0)
    	   beq $t3, 10, exitQ3
    	   loopForDelimeters:    	   
    	     lb $t4, 0($t1)    	   
    	     beq $t4,10,outLoopDelimeter
    	     beq $t3, 32, forSpace
    	     bne $t3, $t4, incrementDelimeter 
    	  forSpace:   
    	     beqz $t2, nextCounterOuterLoop
    	  
    	  afterLastDelimeter:
    	     add $sp, $sp, $t2
    	     addi $sp, $sp,-1
    	     
    	     printSubStrings:
    	        beqz $t2, newlineForQ3
    	        li $v0, 11
    	     	lb $a0, 0($sp)
    	     	syscall
    	     	addi $sp, $sp, -1
    	     	addi $t2, $t2, -1
    	     	j printSubStrings
    	     	
    	     incrementDelimeter:
    	        addi $t1, $t1, 1
    	        j loopForDelimeters
    	
    	   outLoopDelimeter:
    	     addi $sp, $sp, -1
    	     sb $t3, 0($sp)
    	     addi $t2, $t2,1
    	   nextCounterOuterLoop:
    	     addi $t0, $t0,1
    	     move $t1, $s1
    	     j mainLoopQ3
    	     
    	     
    	newlineForQ3:
    	  li $v0, 4
    	  la $a0, newLine_text    #adds new line after printing proper substring
    	  syscall 
    	  j nextCounterOuterLoop   	  
    	  
    	exitQ3:
    	bnez $t2, afterLastDelimeter  #after the last delimeter, if there is still string in the end, goes back and print them
    	
    	j while

question4:
	li $v0, 4
    	la $a0, wecouldnt_message
    	syscall
    	
    	j while
	
