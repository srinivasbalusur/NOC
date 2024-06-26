/* Printing wires     */
wire cb_in_router_0_out0;
wire cb_in_router_0_out1;
wire cb_in_router_0_out2;
wire cb_in_router_0_out3;
wire [0:5] cb_in_router_0_sel;


/* Printing wires     */
wire cb_out_router_0_in0;
wire cb_out_router_0_in1;
wire cb_out_router_0_in2;
wire cb_out_router_0_in3;
wire [0:5] cb_out_router_0_sel;


Demo1_altera_merlin_router_1920_en6jvea router_001 (
	 .sink_valid(cb_in_router_0_out0),
	 .sink_startofpacket(cb_in_router_0_out1),
	 .sink_endofpacket(cb_in_router_0_out2),
	 .src_ready(cb_in_router_0_out3),
	 .sink_ready(cb_out_router_0_in0),
	 .src_valid(cb_out_router_0_in1),
	 .src_startofpacket(cb_out_router_0_in2),
	 .src_endofpacket(cb_out_router_0_in3),
	 .sink_data(intel_niosv_m_0_data_manager_agent_read_cp_data),
	 .clk(clock_in_out_clk_clk),
	 .reset(intel_niosv_m_0_reset_reset_bridge_in_reset_reset),
	 .src_data(router_001_src_data),
	 .src_channel(router_001_src_channel)
);


crbar4x4 cb_in_router_0 (
	 .in0(intel_niosv_m_0_data_manager_agent_read_cp_startofpacket),
	 .in1(intel_niosv_m_0_data_manager_agent_read_cp_endofpacket),
	 .in2(router_001_src_ready),
	 .in3(intel_niosv_m_0_data_manager_agent_read_cp_valid),
	 .out0(cb_in_router_0_out0),
	 .out1(cb_in_router_0_out1),
	 .out2(cb_in_router_0_out2),
	 .out3(cb_in_router_0_out3),
	 .sel0(cb_in_router_0_sel)
);


crbar4x4 cb_out_router_0 (
	 .in0(cb_out_router_0_in0),
	 .in1(cb_out_router_0_in1),
	 .in2(cb_out_router_0_in2),
	 .in3(cb_out_router_0_in3),
	 .out0(sink_ready),
	 .out1(src_valid),
	 .out2(src_startofpacket),
	 .out3(src_endofpacket),
	 .sel0(cb_out_router_0_sel)
);


/* Printing wires     */
wire cb_in_router_1_out0;
wire cb_in_router_1_out1;
wire cb_in_router_1_out2;
wire cb_in_router_1_out3;
wire [0:5] cb_in_router_1_sel;


/* Printing wires     */
wire cb_out_router_1_in0;
wire cb_out_router_1_in1;
wire cb_out_router_1_in2;
wire cb_out_router_1_in3;
wire [0:5] cb_out_router_1_sel;


Demo1_altera_merlin_router_1920_kxovaay router_002 (
	 .sink_valid(cb_in_router_1_out0),
	 .sink_startofpacket(cb_in_router_1_out1),
	 .sink_endofpacket(cb_in_router_1_out2),
	 .src_ready(cb_in_router_1_out3),
	 .sink_ready(cb_out_router_1_in0),
	 .src_valid(cb_out_router_1_in1),
	 .src_startofpacket(cb_out_router_1_in2),
	 .src_endofpacket(cb_out_router_1_in3),
	 .sink_data(intel_niosv_m_0_instruction_manager_agent_write_cp_data),
	 .clk(clock_in_out_clk_clk),
	 .reset(intel_niosv_m_0_reset_reset_bridge_in_reset_reset),
	 .src_data(router_002_src_data),
	 .src_channel(router_002_src_channel)
);


crbar4x4 cb_in_router_1 (
	 .in0(intel_niosv_m_0_instruction_manager_agent_write_cp_startofpacket),
	 .in1(router_002_src_ready),
	 .in2(intel_niosv_m_0_instruction_manager_agent_write_cp_endofpacket),
	 .in3(intel_niosv_m_0_instruction_manager_agent_write_cp_valid),
	 .out0(cb_in_router_1_out0),
	 .out1(cb_in_router_1_out1),
	 .out2(cb_in_router_1_out2),
	 .out3(cb_in_router_1_out3),
	 .sel0(cb_in_router_1_sel)
);


crbar4x4 cb_out_router_1 (
	 .in0(cb_out_router_1_in0),
	 .in1(cb_out_router_1_in1),
	 .in2(cb_out_router_1_in2),
	 .in3(cb_out_router_1_in3),
	 .out0(sink_ready),
	 .out1(src_valid),
	 .out2(src_startofpacket),
	 .out3(src_endofpacket),
	 .sel0(cb_out_router_1_sel)
);


/* Printing wires     */
wire cb_in_router_2_out0;
wire cb_in_router_2_out1;
wire cb_in_router_2_out2;
wire cb_in_router_2_out3;
wire [0:5] cb_in_router_2_sel;


/* Printing wires     */
wire cb_out_router_2_in0;
wire cb_out_router_2_in1;
wire cb_out_router_2_in2;
wire cb_out_router_2_in3;
wire [0:5] cb_out_router_2_sel;


Demo1_altera_merlin_router_1920_kxovaay router_003 (
	 .sink_valid(cb_in_router_2_out0),
	 .sink_startofpacket(cb_in_router_2_out1),
	 .sink_endofpacket(cb_in_router_2_out2),
	 .src_ready(cb_in_router_2_out3),
	 .sink_ready(cb_out_router_2_in0),
	 .src_valid(cb_out_router_2_in1),
	 .src_startofpacket(cb_out_router_2_in2),
	 .src_endofpacket(cb_out_router_2_in3),
	 .sink_data(intel_niosv_m_0_instruction_manager_agent_read_cp_data),
	 .clk(clock_in_out_clk_clk),
	 .reset(intel_niosv_m_0_reset_reset_bridge_in_reset_reset),
	 .src_data(router_003_src_data),
	 .src_channel(router_003_src_channel)
);


crbar4x4 cb_in_router_2 (
	 .in0(intel_niosv_m_0_instruction_manager_agent_read_cp_startofpacket),
	 .in1(router_003_src_ready),
	 .in2(intel_niosv_m_0_instruction_manager_agent_read_cp_valid),
	 .in3(intel_niosv_m_0_instruction_manager_agent_read_cp_endofpacket),
	 .out0(cb_in_router_2_out0),
	 .out1(cb_in_router_2_out1),
	 .out2(cb_in_router_2_out2),
	 .out3(cb_in_router_2_out3),
	 .sel0(cb_in_router_2_sel)
);


crbar4x4 cb_out_router_2 (
	 .in0(cb_out_router_2_in0),
	 .in1(cb_out_router_2_in1),
	 .in2(cb_out_router_2_in2),
	 .in3(cb_out_router_2_in3),
	 .out0(sink_ready),
	 .out1(src_valid),
	 .out2(src_startofpacket),
	 .out3(src_endofpacket),
	 .sel0(cb_out_router_2_sel)
);


/* Printing wires     */
wire cb_in_router_3_out0;
wire cb_in_router_3_out1;
wire cb_in_router_3_out2;
wire cb_in_router_3_out3;
wire [0:5] cb_in_router_3_sel;


/* Printing wires     */
wire cb_out_router_3_in0;
wire cb_out_router_3_in1;
wire cb_out_router_3_in2;
wire cb_out_router_3_in3;
wire [0:5] cb_out_router_3_sel;


Demo1_altera_merlin_router_1920_7io6p2i router_007 (
	 .sink_valid(cb_in_router_3_out0),
	 .sink_startofpacket(cb_in_router_3_out1),
	 .sink_endofpacket(cb_in_router_3_out2),
	 .src_ready(cb_in_router_3_out3),
	 .sink_ready(cb_out_router_3_in0),
	 .src_valid(cb_out_router_3_in1),
	 .src_startofpacket(cb_out_router_3_in2),
	 .src_endofpacket(cb_out_router_3_in3),
	 .sink_data(intel_niosv_m_0_timer_sw_agent_agent_rp_data),
	 .clk(clock_in_out_clk_clk),
	 .reset(intel_niosv_m_0_reset_reset_bridge_in_reset_reset),
	 .src_data(router_007_src_data),
	 .src_channel(router_007_src_channel)
);


crbar4x4 cb_in_router_3 (
	 .in0(intel_niosv_m_0_timer_sw_agent_agent_rp_startofpacket),
	 .in1(intel_niosv_m_0_timer_sw_agent_agent_rp_valid),
	 .in2(intel_niosv_m_0_timer_sw_agent_agent_rp_endofpacket),
	 .in3(router_007_src_ready),
	 .out0(cb_in_router_3_out0),
	 .out1(cb_in_router_3_out1),
	 .out2(cb_in_router_3_out2),
	 .out3(cb_in_router_3_out3),
	 .sel0(cb_in_router_3_sel)
);


crbar4x4 cb_out_router_3 (
	 .in0(cb_out_router_3_in0),
	 .in1(cb_out_router_3_in1),
	 .in2(cb_out_router_3_in2),
	 .in3(cb_out_router_3_in3),
	 .out0(sink_ready),
	 .out1(src_valid),
	 .out2(src_startofpacket),
	 .out3(src_endofpacket),
	 .sel0(cb_out_router_3_sel)
);


/* Printing wires     */
wire cb_in_router_4_out0;
wire cb_in_router_4_out1;
wire cb_in_router_4_out2;
wire cb_in_router_4_out3;
wire [0:5] cb_in_router_4_sel;


/* Printing wires     */
wire cb_out_router_4_in0;
wire cb_out_router_4_in1;
wire cb_out_router_4_in2;
wire cb_out_router_4_in3;
wire [0:5] cb_out_router_4_sel;


Demo1_altera_merlin_router_1920_7io6p2i router_004 (
	 .sink_valid(cb_in_router_4_out0),
	 .sink_startofpacket(cb_in_router_4_out1),
	 .sink_endofpacket(cb_in_router_4_out2),
	 .src_ready(cb_in_router_4_out3),
	 .sink_ready(cb_out_router_4_in0),
	 .src_valid(cb_out_router_4_in1),
	 .src_startofpacket(cb_out_router_4_in2),
	 .src_endofpacket(cb_out_router_4_in3),
	 .sink_data(jtag_uart_0_avalon_jtag_slave_agent_rp_data),
	 .clk(clock_in_out_clk_clk),
	 .reset(intel_niosv_m_0_reset_reset_bridge_in_reset_reset),
	 .src_data(router_004_src_data),
	 .src_channel(router_004_src_channel)
);


crbar4x4 cb_in_router_4 (
	 .in0(jtag_uart_0_avalon_jtag_slave_agent_rp_valid),
	 .in1(jtag_uart_0_avalon_jtag_slave_agent_rp_endofpacket),
	 .in2(jtag_uart_0_avalon_jtag_slave_agent_rp_startofpacket),
	 .in3(router_004_src_ready),
	 .out0(cb_in_router_4_out0),
	 .out1(cb_in_router_4_out1),
	 .out2(cb_in_router_4_out2),
	 .out3(cb_in_router_4_out3),
	 .sel0(cb_in_router_4_sel)
);


crbar4x4 cb_out_router_4 (
	 .in0(cb_out_router_4_in0),
	 .in1(cb_out_router_4_in1),
	 .in2(cb_out_router_4_in2),
	 .in3(cb_out_router_4_in3),
	 .out0(sink_ready),
	 .out1(src_valid),
	 .out2(src_startofpacket),
	 .out3(src_endofpacket),
	 .sel0(cb_out_router_4_sel)
);


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
