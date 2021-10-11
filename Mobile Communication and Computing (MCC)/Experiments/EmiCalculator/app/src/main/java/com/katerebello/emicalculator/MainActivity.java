package com.katerebello.emicalculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import android.widget.TextView;

import java.text.DecimalFormat;
//import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private Button calc_button;
    private EditText principal_text;
    private EditText rate_text;
    private EditText time_text;
    private TextView res_text;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        findViews();
//        String test="Alert!!";
//        Toast.makeText(this, test, Toast.LENGTH_LONG).show();
//        result.setText("I can change text!!");
        onClickButton();
    }

    private void onClickButton() {
        calc_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                Toast.makeText(MainActivity.this, "YOU ARE FAT!!", Toast.LENGTH_LONG).show();
                double emi = emiCalculator();
                if (emi == 0.0) {
                    guide();
                }
                else {
                    display(emi);
                }
            }
        });
    }

    private double emiCalculator() {

        double p = Double.parseDouble(principal_text.getText().toString());
        double r = Double.parseDouble(rate_text.getText().toString());
        double n = Integer.parseInt(time_text.getText().toString());


        //double rate= (r/1200);
        //double result = (p * rate * Math.pow(1 + rate, n) / Math.pow(1 + rate, n) - 1);

        double principal  = p;

        double rate= (r/1200);
        //System.out.println(rate);

        double emi = (principal * rate * Math.pow(1 + rate, n)) / (Math.pow(1 + rate, n)-1);
        //System.out.println(res);

        return emi;
    }

    private void guide() {
        String result = "";
        res_text.setText(result);
    }

    private void display(double emi) {
        DecimalFormat df = new DecimalFormat("0.00");
        String result = df.format(emi);

        res_text.setText(result);
    }

    private void findViews() {

        principal_text = findViewById(R.id.principal_edit_text);
        rate_text = findViewById(R.id.rate_edit_text);
        time_text = findViewById(R.id.time_edit_text);
        calc_button = findViewById(R.id.calculate_button);
        res_text = findViewById(R.id.res_text);
    }
}