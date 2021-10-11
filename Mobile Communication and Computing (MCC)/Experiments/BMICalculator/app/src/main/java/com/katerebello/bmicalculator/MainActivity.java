package com.katerebello.bmicalculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        String test = "Wohooo!,I can make an alert pop!";
        Toast.makeText(this,test,Toast.LENGTH_LONG).show();

        RadioButton male_radiobutton  = findViewById(R.id.male_radio_button);
        RadioButton female_radiobutton  = findViewById(R.id.female_radio_button);
        EditText age_edittext  = findViewById(R.id.age_edit_text);
        EditText feet_edittext = findViewById(R.id.feet_edit_text);
        EditText inches_edittext = findViewById(R.id.inches_edit_text);
        EditText wt_edittext = findViewById(R.id.wt_edit_text);
        Button calculate_button = findViewById(R.id.calculate_button);
        TextView result_text = findViewById(R.id.displaytext);

        result_text.setText("18.5");


        calculate_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Toast.makeText(MainActivity.this,"18.5",Toast.LENGTH_LONG).show();



            }
        });


    }
}