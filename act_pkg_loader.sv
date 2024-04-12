wire [59:0] select_lines;

assign cb_in_router_0_sel = select_lines[5:0];
assign cb_out_router_0_sel = select_lines[11:6];
assign cb_in_router_1_sel = select_lines[17:12];
assign cb_out_router_1_sel = select_lines[23:18];
assign cb_in_router_2_sel = select_lines[29:24];
assign cb_out_router_2_sel = select_lines[35:30];
assign cb_in_router_3_sel = select_lines[41:36];
assign cb_out_router_3_sel = select_lines[47:42];
assign cb_in_router_4_sel = select_lines[53:48];
assign cb_out_router_4_sel = select_lines[59:54];

activation_package_n_bit act1 (
	.clk(clock_in_out_clk_clk),
	.reset(intel_niosv_m_0_reset_reset_bridge_in_reset_reset),
	.serial_in(serial_in),
	.parallel_out(select_lines)
);