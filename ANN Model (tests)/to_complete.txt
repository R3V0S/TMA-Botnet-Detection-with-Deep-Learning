Done:
	- Dropped unnecessary columns:
		- StartTime
		- DstAddr
		- SrcAddr (provisionary)
		- State (provisionary)
		
	- Mapped columns to int64
		- Proto
		- Dir
		
	- Dropped columns with NaNs:
		- Error --> Sport and Dport are dropped --> wrong information --> MUST BE CHECKED
		
To Do:
	- Check ports problem
	- Check what are States
		- we need to keep it?
		- If so, we mapped it?
	- SrcAddr is necessary?
		- maybe depends on the attack?
		- SrcAddr could be a botnet device addr?
			- flag == ...botnet... refers to an attack from a botnet or an infection attack to create a botnet?