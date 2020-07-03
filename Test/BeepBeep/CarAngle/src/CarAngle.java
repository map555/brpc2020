import ca.uqac.lif.cep.Connector;
import ca.uqac.lif.cep.Pullable;
import ca.uqac.lif.cep.functions.ApplyFunction;
import ca.uqac.lif.cep.functions.FunctionTree;
import ca.uqac.lif.cep.io.ReadLines;
import ca.uqac.lif.cep.io.WriteToFile;
import ca.uqac.lif.cep.json.JPathFunction;
import ca.uqac.lif.cep.json.NumberValue;
import ca.uqac.lif.cep.json.ParseJson;
import ca.uqac.lif.cep.mtnp.DrawPlot;
import ca.uqac.lif.cep.mtnp.UpdateTable;
import ca.uqac.lif.cep.mtnp.UpdateTableStream;
import ca.uqac.lif.cep.tmf.Fork;
import ca.uqac.lif.cep.tmf.KeepLast;
import ca.uqac.lif.cep.tmf.Pump;
import ca.uqac.lif.cep.tmf.QueueSource;
import ca.uqac.lif.cep.util.Numbers;
import ca.uqac.lif.json.JsonElement;
import ca.uqac.lif.json.JsonMap;
import ca.uqac.lif.mtnp.plot.gnuplot.Scatterplot;

import java.io.InputStream;

public class CarAngle {
    public static void main(String[] args) {
        InputStream is=CarAngle.class.getResourceAsStream("d6.txt");
        ReadLines reader=new ReadLines(is);
        Pullable rp=reader.getPullableOutput();



        ApplyFunction parseData=new ApplyFunction(ParseJson.instance);
        ApplyFunction jpfData=new ApplyFunction(new JPathFunction("data.position and direction.direction"));
        Fork dataFork=new Fork(2);
        Fork angleForkX=new Fork(2);
        Fork angleForkY=new Fork(2);
        ApplyFunction jpfX=new ApplyFunction((new FunctionTree(NumberValue.instance, new JPathFunction("x"))));
        ApplyFunction jpfY=new ApplyFunction((new FunctionTree(NumberValue.instance, new JPathFunction("y"))));
        ApplyFunction absoluteX=new ApplyFunction(Numbers.absoluteValue);
        ApplyFunction absoluteY=new ApplyFunction(Numbers.absoluteValue);
        ApplyFunction quadrant=new ApplyFunction(new getQuadrant());
        ApplyFunction adjustment=new ApplyFunction(new QuadrantAjustement());

        QueueSource xAxisTableSource=new QueueSource().loop(false);
        KeepLast kl=new KeepLast();
        ApplyFunction arctan=new ApplyFunction(new ArcTangent());
        UpdateTable angleTable=new UpdateTableStream("time(second)","angle(degree)");
        DrawPlot draw= new DrawPlot(new Scatterplot());
        Pullable p=draw.getPullableOutput();
        WriteToFile w =new WriteToFile("CarAngle6.png");
        Pump pump=new Pump();

        Connector.connect(reader,parseData);
        Connector.connect(parseData,jpfData);
        Connector.connect(jpfData,dataFork);
        Connector.connect(dataFork,0,jpfX,0);
        Connector.connect(dataFork,1,jpfY,0);
        Connector.connect(jpfX,angleForkX);
        Connector.connect(jpfY,angleForkY);

        Connector.connect(angleForkX,1,absoluteX,0);
        Connector.connect(angleForkY,1,absoluteY,0);
        Connector.connect(absoluteX,0,arctan,0);
        Connector.connect(absoluteY,0,arctan,1);
        Connector.connect(angleForkX,0,quadrant,0);
        Connector.connect(angleForkY,0,quadrant,1);
        Connector.connect(quadrant,0,adjustment,0);
        Connector.connect(arctan,0,adjustment,1);


        Connector.connect(xAxisTableSource,0,angleTable,0);
        Connector.connect(adjustment,0,angleTable,1);
        Connector.connect(angleTable,kl);
        Connector.connect(kl,draw);
        Connector.connect(kl,w);
        Connector.connect(pump,w);
        Connector.connect(draw,pump);





        double time=0;

        //note: in this test code, the data aquisition rate per second is hardcoded

        while(time<30.1){

            xAxisTableSource.addEvent(time);
            time=time+0.10;


        }
        pump.run();

    }
    public static JsonMap getSubDict(JsonMap dict,String wantedDictName){
        Object[] out = new Object[1];
        JPathFunction data=new JPathFunction(wantedDictName);
        data.evaluate(new Object[]{dict},out);
        JsonMap subDict=(JsonMap) out[0];

        return subDict;

    }

    public static Object getData(JsonMap dict,String elementName){
        Object data= dict.getNumber(elementName);

        return data;

    }
}


