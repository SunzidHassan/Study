using System;

public class Product
{
    public string PartA { get; set; }
    public string PartB { get; set; }
    public string PartC { get; set; }

    public void Display()
    {
        Console.WriteLine($"Part A: {PartA}");
        Console.WriteLine($"Part B: {PartB}");
        Console.WriteLine($"Part C: {PartC}");
    }
}

public abstract class Builder
{
    public abstract void BuildPartA();
    public abstract void BuildPartB();
    public abstract void BuildPartC();
    public abstract Product GetResult();
}

public class ConcreteBuilder : Builder
{
    private readonly Product _product = new Product();

    public override void BuildPartA()
    {
        _product.PartA = "Part A";
    }

    public override void BuildPartB()
    {
        _product.PartB = "Part B";
    }

    public override void BuildPartC()
    {
        _product.PartC = "Part C";
    }

    public override Product GetResult()
    {
        return _product;
    }
}

public class Director
{
    private readonly Builder _builder;

    public Director(Builder builder)
    {
        _builder = builder;
    }

    public void Construct()
    {
        _builder.BuildPartA();
        _builder.BuildPartB();
        _builder.BuildPartC();
    }
}

class Program
{
    static void Main(string[] args)
    {
        var builder = new ConcreteBuilder();
        var director = new Director(builder);
        director.Construct();

        var product = builder.GetResult();
        product.Display();
    }
}
