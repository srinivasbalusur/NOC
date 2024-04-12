// Intel-NOC
// Maneesh Merugu
// Srinivas Balusu
// Crossbar Implementation

//2x2 crossbar module
module crbar2x2
	(
	input wire in0,
	input wire in1,
	input wire sel,
	output wire out0,
	output wire out1
	);
	
	assign out0=((~sel&in0)|(sel&in1));
	assign out1=((~sel&in1)|(sel&in0));
endmodule

//4x4 crossbar module using 6 2x2 crossbar modules
module crbar4x4 
	(
	input wire in0,
	input wire in1,
	input wire in2,
	input wire in3,
	input wire [5:0] sel0,
	output wire out0,
	output wire out1,
	output wire out2,
	output wire out3
	);
	
	wire  crbar1_1out,crbar1_2out;
	wire  crbar2_1out,crbar2_2out;
	wire  crbar4_1out,crbar4_2out;
	wire  crbar5_1out,crbar5_2out;
	

	crbar2x2 crbar1 (.in0(in0), .in1(in1), .sel(sel0[0]), .out0(crbar1_1out), .out1(crbar1_2out));
	crbar2x2 crbar2 (.in0(crbar1_1out), .in1(crbar4_1out), .sel(sel0[1]), .out0(crbar2_1out), .out1(crbar2_2out));
	crbar2x2 crbar3 (.in0(crbar2_1out), .in1(crbar5_1out), .sel(sel0[2]), .out0(out0), .out1(out1));
	crbar2x2 crbar4 (.in0(in2), .in1(in3), .sel(sel0[3]), .out0(crbar4_1out), .out1(crbar4_2out));
	crbar2x2 crbar5 (.in0(crbar1_2out), .in1(crbar4_2out), .sel(sel0[4]), .out0(crbar5_1out), .out1(crbar5_2out));
	crbar2x2 crbar6 (.in0(crbar2_2out), .in1(crbar5_2out), .sel(sel0[5]), .out0(out2), .out1(out3));
endmodule



