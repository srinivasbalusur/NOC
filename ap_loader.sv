
// Intel-NOC
// Maneesh Merugu
// Srinivas Balusu
// Activation Package Implementation


//Module code
module activation_package_n_bit
	(
	input wire clk,
    input wire reset,
    input wire serial_in,
    output wire [59:0] parallel_out
	);

    reg [59:0] register;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            register <= 60'b0;
        end else begin
            register <= {register[58:0],serial_in};
        end
    end
	
    assign parallel_out = register;
	
endmodule
