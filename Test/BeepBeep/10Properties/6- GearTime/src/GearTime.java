import ca.uqac.lif.cep.Connector;
import ca.uqac.lif.cep.Pullable;
import ca.uqac.lif.cep.functions.ApplyFunction;
import ca.uqac.lif.cep.functions.FunctionTree;
import ca.uqac.lif.cep.io.ReadLines;
import ca.uqac.lif.cep.json.JPathFunction;
import ca.uqac.lif.cep.json.NumberValue;
import ca.uqac.lif.cep.json.ParseJson;
import ca.uqac.lif.cep.tmf.Fork;
import ca.uqac.lif.json.JsonElement;
import ca.uqac.lif.json.JsonMap;

import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.text.DecimalFormat;

/************************************************
 * @Description: Returns the amount of time spent in each Gear during the testing period.
 *
 * @Input: BeamNGpy Dictionary.
 *
 * @Output: Writes the results in 6 separate lines from Gear 1 to 6
 ***********************************************/

public class GearTime {

    public static void main(String[] args)
    {
        Number time0, time1;
        double deltatime;
        int currentGear = 0;
        deltatime = 0;
        time0 = 0;

        // Set up an array, containing the time spent into each gear.

        Double gearTime[] = new Double[]{0.0,0.0,0.0,0.0,0.0,0.0};
		
        // Open up the dictionnary

        InputStream is=GearTime.class.getResourceAsStream("data.txt");
        ReadLines reader= new ReadLines(is);

        // Set up the BeepBeep Modules for data collection

        ApplyFunction parseData = new ApplyFunction(ParseJson.instance);
        ApplyFunction jpfGear = new ApplyFunction((new FunctionTree(NumberValue.instance, new JPathFunction("data.transmission.actualGear"))));
        ApplyFunction jpfTime = new ApplyFunction(new JPathFunction("time"));

        Fork dictFork= new Fork(2);

        Connector.connect(reader, parseData);

        Connector.connect(parseData, dictFork);
        Connector.connect(dictFork,0,jpfGear,0);
        Connector.connect(dictFork,0,jpfTime,0);

        Connector.connect(parseData, jpfGear);

        Pullable pTime= jpfTime.getPullableOutput();
        Pullable pGear= jpfGear.getPullableOutput();

        // Grab the gear for each data collected, then send it to to the right array index.

        while (pGear.hasNext())
        {
            currentGear = ((Number) pGear.pull()).intValue();
            time1 = convertTime(pTime.pull().toString());
            deltatime = time1.doubleValue() - time0.doubleValue();
            gearTime[currentGear] = gearTime[currentGear] + deltatime;
            time0 = time1;
        }

        System.out.println("Gear 0 = " + gearTime[0]/1000 + " s");
        System.out.println("Gear 1 = " + gearTime[1]/1000 + " s");
        System.out.println("Gear 2 = " + gearTime[2]/1000 + " s");
        System.out.println("Gear 3 = " + gearTime[3]/1000 + " s");
        System.out.println("Gear 4 = " + gearTime[4]/1000 + " s");
        System.out.println("Gear 5 = " + gearTime[5]/1000 + " s");

        if (args.length == 1) {
            // Write result

            try {
                DecimalFormat decimalFormat = new DecimalFormat("#.000");//keep three decimal places

                FileWriter resultWriter = new FileWriter(args[0] + "GearTimeResults.txt");

                resultWriter.write("Gear0: " + decimalFormat.format(gearTime[0]) + " s"+"\n"
                                    +"Gear1: " + decimalFormat.format(gearTime[1]) + " s"+"\n"
                                    +"Gear2: "+ decimalFormat.format(gearTime[2]) + " s"+"\n"
                                    +"Gear3: "+ decimalFormat.format(gearTime[3]) + " s"+"\n"
                                    +"Gear4: "+ decimalFormat.format(gearTime[4]) + " s"+"\n"
                                    +"Gear5: "+ decimalFormat.format(gearTime[5]) + " s");

                resultWriter.close();
            }

            catch (IOException e) {
                System.out.println("An error occurred.");
                e.printStackTrace();
            }

        }


    }

    // Convert the time string into a numeral value represented in Ms

    public static double convertTime(String timeString) {
        timeString = timeString.replaceAll("\"", "");
        String[] tokens = timeString.split(":");
        String[] secondsTokens = tokens[2].split("\\.");
        int Ms = Integer.parseInt(secondsTokens[1]);
        Ms = Ms / 1000;
        int secondsToMs = Integer.parseInt(secondsTokens[0]) * 1000;
        int minutesToMs = Integer.parseInt(tokens[1]) * 60000;
        int hoursToMs = Integer.parseInt(tokens[0]) * 3600000;
        long totalMs = secondsToMs + minutesToMs + hoursToMs + Ms;
        return totalMs;

    }


}
