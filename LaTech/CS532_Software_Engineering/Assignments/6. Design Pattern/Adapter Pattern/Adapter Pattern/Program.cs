// The 'Target' interface
public interface IWeightConverter
{
    double ToLb(double kg);
}

// Adaptee class
public class KgToLb
{
    public double Convert(double kg)
    {
        return kg * 2.20462;
    }
}

// Adapter class
public class WeightAdapter : IWeightConverter
{
    private KgToLb converter;

    public WeightAdapter(KgToLb converter)
    {
        this.converter = converter;
    }

    public double ToLb(double kg)
    {
        // Use the KgToLb to convert the weight
        return converter.Convert(kg);
    }
}

// Client class
public class Client
{
    static void Main(string[] args)
    {
        // kg value to convert
        double kg = 10;

        // Create adapter to convert kg to lb
        IWeightConverter adapter = new WeightAdapter(new KgToLb());
        double Lb = adapter.ToLb(kg);

        // Display result
        Console.WriteLine($"{kg} kg is equal to {Lb} lb");
    }
}
