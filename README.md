<H1> Circuit Solver </H1>
<P>
A project based on solving voltages and currents using graph theory.Circuits are represented as collection of nodes and branches and the soluton is obtained by generating the fundamental loop, cutset, impedance, admittance matrices.
<br>
<H2> Installation instructions- </H2>
<H3> With pip </H3>
  <ul> 
    <li> Install dependencies using pip: pip install -r requirements.txt 
    </li>
  </ul>
<H3> Usage </H3>
  <ul>
    <li> Run run.py
    </li> 
    <li> Arguments-<br> 
      <ol type=i> 
        <li>filename- name of the input file
  </ul>
<H2> Instructions for writing the input- </H2>
<ul> 
<li> Sequence to be followed - [Branch source node, Branch destination node, Resistance in branch,Capacitance in branch,Inductance in branch,Associated voltage source,Associated current source ] </li>
<li> While writing voltages and currents maintain the format asspecified in conversions.txt.
<li> Units- <br> For accepted units and abbrevation- see conversions.txt. <br>Note- The units like Ohm, Volts, Amperes should be omitted while providing the input.
<li> Input is parsed based on space seperation. 
</ul>

<H3> What is remaining- </H3>
<ul> <li> argument parsing 
