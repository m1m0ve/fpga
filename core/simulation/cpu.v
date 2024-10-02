`default_nettype none

module cpu(
    input wire clk,
    output wire [3:0] led
);

    // 25-bit counter (for slower LED movement)
    reg [24:0] counter = 0;
    
    // 2-bit state to control which LED is on
    reg [1:0] led_state = 0;

    always @(posedge clk) begin
        // Increment the counter every clock cycle
        counter <= counter + 1;
        $display("Blink");
        
        // Change LED state when counter reaches its maximum value
        if (counter == 0) begin
            led_state <= led_state + 1;
        end
    end

    // Assign LED outputs based on current state
    assign led[0] = (led_state == 2'b00);
    assign led[1] = (led_state == 2'b01);
    assign led[2] = (led_state == 2'b10);
    assign led[3] = (led_state == 2'b11);

endmodule
