Lab 02: Linux Process Management & Network Basics
Date: 14/01/2026
Status: Completed
Environment: Kali Linux (VirtualBox)
1. Objective
Simulate a Systems Administrator role to identify and terminate a "ghost" process consuming resources and detect an unauthorized open port (Backdoor).
2. Technical Steps
A. The Ghost Process (Process Management)
I created a background process to simulate a resource hog.
code
Bash
sleep 1000 &
Hunting the PID:
I used ps combined with grep to filter the process list.
code
Bash
ps aux | grep sleep
Output:
code
Text
nightwe+ 45349 0.0 0.0 3020 1628 pts/3 SN 14:44 0:00 sleep 1000
Termination:
I identified PID 45349 and terminated it gracefully using SIGTERM (-15).
code
Bash
kill -15 45349
# Output: [1] + terminated sleep 1000
B. The Backdoor (Networking & Ports)
I used netcat to open a listener on port 4444 (simulating a backdoor).
code
Bash
nc -lvnp 4444
Port Verification:
In a second terminal, I verified the port was open and listening using netstat.
code
Bash
sudo netstat -tulpn
Evidence (Missing in original, added here):
Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  3      [ ]         DGRAM      CONNECTED     6011     
unix  3      [ ]         STREAM     CONNECTED     10586    /run/user/1000/bus
unix  3      [ ]         DGRAM      CONNECTED     1413     
unix  3      [ ]         STREAM     CONNECTED     12562    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     9731     @/tmp/.ICE-unix/1182
unix  3      [ ]         STREAM     CONNECTED     9668     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     5938     
unix  2      [ ]         DGRAM      CONNECTED     44750    
unix  3      [ ]         STREAM     CONNECTED     11548    /run/dbus/system_bus_socket
unix  3      [ ]         DGRAM      CONNECTED     6010     
unix  3      [ ]         DGRAM      CONNECTED     1417     
unix  3      [ ]         STREAM     CONNECTED     12457    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     12441    /run/user/1000/at-spi/bus_0
unix  3      [ ]         DGRAM      CONNECTED     7611     
unix  3      [ ]         STREAM     CONNECTED     12538    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     13462    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     12445    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     10982    
unix  3      [ ]         STREAM     CONNECTED     10528    
unix  3      [ ]         STREAM     CONNECTED     10367    /run/dbus/system_bus_socket
unix  3      [ ]         DGRAM      CONNECTED     7483     
unix  3      [ ]         STREAM     CONNECTED     10090    
unix  3      [ ]         STREAM     CONNECTED     77253    /run/user/1000/bus
unix  3      [ ]         DGRAM      CONNECTED     1415     
unix  3      [ ]         STREAM     CONNECTED     12945    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     13417    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     12397    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     102769   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     10588    
unix  3      [ ]         DGRAM      CONNECTED     6009     
unix  3      [ ]         STREAM     CONNECTED     13412    
unix  3      [ ]         STREAM     CONNECTED     10525    
unix  3      [ ]         DGRAM      CONNECTED     7634     
unix  3      [ ]         STREAM     CONNECTED     76291    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     103561   
unix  3      [ ]         STREAM     CONNECTED     14413    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     13402    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     10984    
unix  3      [ ]         STREAM     CONNECTED     10536    
unix  3      [ ]         STREAM     CONNECTED     10088    
unix  3      [ ]         STREAM     CONNECTED     10694    /run/user/1000/bus
unix  2      [ ]         DGRAM      CONNECTED     5992     
unix  3      [ ]         STREAM     CONNECTED     10981    
unix  3      [ ]         STREAM     CONNECTED     10537    
unix  3      [ ]         STREAM     CONNECTED     13394    
unix  3      [ ]         STREAM     CONNECTED     7473     
unix  3      [ ]         STREAM     CONNECTED     11615    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     14760    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     12409    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     9810     
unix  3      [ ]         STREAM     CONNECTED     13410    
unix  3      [ ]         STREAM     CONNECTED     9132     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     10540    
unix  3      [ ]         STREAM     CONNECTED     12938    @/tmp/.ICE-unix/1182
unix  3      [ ]         DGRAM      CONNECTED     1416     
unix  3      [ ]         STREAM     CONNECTED     12942    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     12367    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     9809     
unix  3      [ ]         STREAM     CONNECTED     13395    
unix  3      [ ]         STREAM     CONNECTED     10545    
unix  3      [ ]         STREAM     CONNECTED     14485    /run/dbus/system_bus_socket
unix  3      [ ]         DGRAM      CONNECTED     6006     
unix  3      [ ]         STREAM     CONNECTED     12424    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     11457    @/tmp/.ICE-unix/1182
unix  3      [ ]         STREAM     CONNECTED     10988    
unix  3      [ ]         STREAM     CONNECTED     9773     
unix  2      [ ]         DGRAM      CONNECTED     7482     
unix  3      [ ]         STREAM     CONNECTED     12491    @/tmp/.X11-unix/X0
unix  2      [ ]         DGRAM      CONNECTED     5983     
unix  3      [ ]         STREAM     CONNECTED     9811     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12421    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     10523    
unix  3      [ ]         STREAM     CONNECTED     8861     
unix  3      [ ]         DGRAM      CONNECTED     7484     
unix  3      [ ]         STREAM     CONNECTED     75759    
unix  3      [ ]         DGRAM      CONNECTED     6008     
unix  3      [ ]         STREAM     CONNECTED     12948    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     10597    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     9666     /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     13413    
unix  3      [ ]         DGRAM      CONNECTED     7633     
unix  3      [ ]         STREAM     CONNECTED     75758    
unix  3      [ ]         STREAM     CONNECTED     5445     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     1942     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9830     
unix  3      [ ]         STREAM     CONNECTED     13408    
unix  3      [ ]         STREAM     CONNECTED     10532    
unix  3      [ ]         STREAM     CONNECTED     75760    
unix  3      [ ]         STREAM     CONNECTED     10087    
unix  3      [ ]         DGRAM      CONNECTED     6007     
unix  3      [ ]         DGRAM      CONNECTED     1414     
unix  3      [ ]         STREAM     CONNECTED     14756    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     10584    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     12463    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     13419    
unix  3      [ ]         STREAM     CONNECTED     10585    
unix  2      [ ]         DGRAM      CONNECTED     5932     
unix  3      [ ]         DGRAM      CONNECTED     1418     
unix  3      [ ]         STREAM     CONNECTED     10983    
unix  3      [ ]         STREAM     CONNECTED     9813     
unix  3      [ ]         STREAM     CONNECTED     13401    
unix  3      [ ]         STREAM     CONNECTED     10526    
unix  3      [ ]         DGRAM      CONNECTED     7610     
unix  3      [ ]         STREAM     CONNECTED     14477    
unix  3      [ ]         STREAM     CONNECTED     9748     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     5971     
unix  3      [ ]         STREAM     CONNECTED     9800     
unix  3      [ ]         STREAM     CONNECTED     10534    
unix  3      [ ]         DGRAM      CONNECTED     7639     
unix  2      [ ]         DGRAM      CONNECTED     107844   
unix  3      [ ]         STREAM     CONNECTED     107635   
unix  3      [ ]         STREAM     CONNECTED     12451    
unix  3      [ ]         STREAM     CONNECTED     11627    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     7020     
unix  3      [ ]         STREAM     CONNECTED     12575    
unix  3      [ ]         STREAM     CONNECTED     11508    
unix  3      [ ]         STREAM     CONNECTED     79187    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     13484    
unix  3      [ ]         STREAM     CONNECTED     9741     
unix  3      [ ]         STREAM     CONNECTED     9622     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     6075     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9838     
unix  3      [ ]         STREAM     CONNECTED     12557    
unix  3      [ ]         STREAM     CONNECTED     11343    
unix  3      [ ]         STREAM     CONNECTED     11471    
unix  3      [ ]         STREAM     CONNECTED     6947     
unix  3      [ ]         STREAM     CONNECTED     1679     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     10689    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     13524    
unix  3      [ ]         STREAM     CONNECTED     12573    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     9746     
unix  3      [ ]         STREAM     CONNECTED     9591     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     8991     /run/containerd/containerd.sock
unix  3      [ ]         STREAM     CONNECTED     12572    
unix  3      [ ]         STREAM     CONNECTED     12331    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     11359    
unix  3      [ ]         STREAM     CONNECTED     10639    /run/user/1000/bus
unix  2      [ ]         DGRAM                    6005     /run/user/1000/systemd/notify
unix  3      [ ]         STREAM     CONNECTED     12647    
unix  3      [ ]         STREAM     CONNECTED     14416    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     9750     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     6119     
unix  3      [ ]         STREAM     CONNECTED     9759     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9747     
unix  3      [ ]         STREAM     CONNECTED     6072     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     11372    
unix  3      [ ]         STREAM     CONNECTED     7122     /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     7032     
unix  3      [ ]         STREAM     CONNECTED     12631    
unix  3      [ ]         STREAM     CONNECTED     11484    
unix  3      [ ]         STREAM     CONNECTED     6962     
unix  3      [ ]         STREAM     CONNECTED     107846   
unix  3      [ ]         STREAM     CONNECTED     10083    @/tmp/.X11-unix/X0
unix  2      [ ]         DGRAM      CONNECTED     9843     
unix  3      [ ]         STREAM     CONNECTED     13460    
unix  3      [ ]         STREAM     CONNECTED     9737     
unix  3      [ ]         STREAM     CONNECTED     9203     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9195     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12547    
unix  3      [ ]         STREAM     CONNECTED     11360    
unix  3      [ ]         STREAM     CONNECTED     14436    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     6978     
unix  3      [ ]         DGRAM      CONNECTED     6683     
unix  3      [ ]         STREAM     CONNECTED     12633    
unix  3      [ ]         STREAM     CONNECTED     10641    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     12432    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     6105     
unix  3      [ ]         STREAM     CONNECTED     10423    
unix  3      [ ]         STREAM     CONNECTED     9193     
unix  3      [ ]         STREAM     CONNECTED     8531     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     12502    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     12327    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     14482    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     12454    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     9556     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     10701    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12602    
unix  3      [ ]         STREAM     CONNECTED     12488    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     107847   
unix  3      [ ]         STREAM     CONNECTED     106665   @/tmp/.ICE-unix/1182
unix  3      [ ]         STREAM     CONNECTED     11919    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9752     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9611     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     9840     
unix  3      [ ]         STREAM     CONNECTED     7034     /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     107629   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12554    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     12468    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     12407    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     6094     
unix  3      [ ]         STREAM     CONNECTED     9180     
unix  3      [ ]         STREAM     CONNECTED     6731     
unix  3      [ ]         STREAM     CONNECTED     11606    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     12496    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12565    
unix  3      [ ]         STREAM     CONNECTED     12598    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     9209     /run/systemd/journal/stdout
unix  2      [ ]         DGRAM      CONNECTED     4794     
unix  3      [ ]         STREAM     CONNECTED     43870    
unix  3      [ ]         STREAM     CONNECTED     12428    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     6110     
unix  3      [ ]         STREAM     CONNECTED     10631    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     6998     @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     5607     
unix  3      [ ]         STREAM     CONNECTED     9844     
unix  3      [ ]         STREAM     CONNECTED     12553    
unix  3      [ ]         STREAM     CONNECTED     7031     
unix  3      [ ]         STREAM     CONNECTED     12516    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     11486    
unix  3      [ ]         STREAM     CONNECTED     12412    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     6961     
unix  3      [ ]         STREAM     CONNECTED     8990     
unix  3      [ ]         STREAM     CONNECTED     14423    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     13437    
unix  3      [ ]         STREAM     CONNECTED     10427    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9833     
unix  3      [ ]         STREAM     CONNECTED     12566    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     7037     
unix  3      [ ]         STREAM     CONNECTED     9204     /run/user/1000/bus
unix  3      [ ]         DGRAM      CONNECTED     6684     
unix  3      [ ]         STREAM     CONNECTED     12444    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12333    
unix  3      [ ]         STREAM     CONNECTED     75761    @/tmp/.ICE-unix/1182
unix  3      [ ]         STREAM     CONNECTED     13503    
unix  3      [ ]         STREAM     CONNECTED     11554    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     9734     
unix  3      [ ]         STREAM     CONNECTED     11392    /run/user/1000/pipewire-0-manager
unix  3      [ ]         STREAM     CONNECTED     9832     
unix  2      [ ]         DGRAM                    43869    
unix  3      [ ]         STREAM     CONNECTED     12558    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     7033     
unix  3      [ ]         STREAM     CONNECTED     6073     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     12315    
unix  3      [ ]         STREAM     CONNECTED     6100     
unix  3      [ ]         STREAM     CONNECTED     11611    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     12465    @/tmp/.ICE-unix/1182
unix  3      [ ]         STREAM     CONNECTED     9743     
unix  3      [ ]         STREAM     CONNECTED     5644     
unix  3      [ ]         STREAM     CONNECTED     79188    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     9836     
unix  3      [ ]         STREAM     CONNECTED     104016   /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     9697     /run/user/1000/bus
unix  2      [ ]         DGRAM                    6118     
unix  3      [ ]         STREAM     CONNECTED     13839    
unix  3      [ ]         STREAM     CONNECTED     10671    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     13517    
unix  3      [ ]         STREAM     CONNECTED     9745     
unix  3      [ ]         STREAM     CONNECTED     9579     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     9846     
unix  3      [ ]         STREAM     CONNECTED     12470    
unix  3      [ ]         STREAM     CONNECTED     9625     /run/user/1000/bus
unix  2      [ ]         DGRAM      CONNECTED     12332    
unix  3      [ ]         STREAM     CONNECTED     9205     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12596    
unix  3      [ ]         STREAM     CONNECTED     9725     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     52288    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     13525    
unix  3      [ ]         STREAM     CONNECTED     9753     
unix  3      [ ]         STREAM     CONNECTED     107628   
unix  3      [ ]         STREAM     CONNECTED     9839     
unix  3      [ ]         STREAM     CONNECTED     75756    
unix  3      [ ]         STREAM     CONNECTED     13415    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     13853    
unix  3      [ ]         STREAM     CONNECTED     12577    
unix  3      [ ]         STREAM     CONNECTED     11491    
unix  3      [ ]         STREAM     CONNECTED     13446    
unix  3      [ ]         STREAM     CONNECTED     9735     
unix  3      [ ]         STREAM     CONNECTED     9341     /run/containerd/containerd.sock
unix  3      [ ]         STREAM     CONNECTED     9845     
unix  3      [ ]         STREAM     CONNECTED     12453    
unix  3      [ ]         STREAM     CONNECTED     13857    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     7018     
unix  3      [ ]         STREAM     CONNECTED     75755    
unix  3      [ ]         STREAM     CONNECTED     12600    
unix  3      [ ]         STREAM     CONNECTED     11565    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     12415    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     9724     
unix  3      [ ]         STREAM     CONNECTED     12292    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     11334    
unix  3      [ ]         STREAM     CONNECTED     14458    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     10550    /run/user/1000/at-spi/bus_0
unix  2      [ ]         DGRAM                    11537    
unix  3      [ ]         STREAM     CONNECTED     106664   
unix  3      [ ]         STREAM     CONNECTED     10682    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12438    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     9192     
unix  3      [ ]         STREAM     CONNECTED     11559    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     11390    /run/user/1000/pipewire-0-manager
unix  3      [ ]         STREAM     CONNECTED     6122     
unix  3      [ ]         STREAM     CONNECTED     7115     
unix  3      [ ]         STREAM     CONNECTED     8567     
unix  3      [ ]         STREAM     CONNECTED     6485     
unix  3      [ ]         STREAM     CONNECTED     9550     
unix  3      [ ]         STREAM     CONNECTED     14753    
unix  3      [ ]         STREAM     CONNECTED     12452    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     9707     /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     14715    
unix  3      [ ]         STREAM     CONNECTED     12377    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     9738     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     13389    
unix  3      [ ]         STREAM     CONNECTED     6597     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     12371    
unix  3      [ ]         STREAM     CONNECTED     43866    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     14704    
unix  3      [ ]         STREAM     CONNECTED     12439    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     11443    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9709     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     11916    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12389    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     7102     
unix  3      [ ]         STREAM     CONNECTED     6570     
unix  3      [ ]         STREAM     CONNECTED     51436    
unix  3      [ ]         STREAM     CONNECTED     14721    
unix  3      [ ]         STREAM     CONNECTED     6074     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     12494    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     13392    
unix  3      [ ]         STREAM     CONNECTED     8532     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     11379    
unix  3      [ ]         STREAM     CONNECTED     11630    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     11920    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     9686     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     13378    
unix  3      [ ]         STREAM     CONNECTED     14484    
unix  3      [ ]         STREAM     CONNECTED     14735    
unix  3      [ ]         STREAM     CONNECTED     5853     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     7134     
unix  3      [ ]         STREAM     CONNECTED     12395    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     6596     
unix  2      [ ]         DGRAM      CONNECTED     8323     
unix  3      [ ]         STREAM     CONNECTED     14755    
unix  3      [ ]         STREAM     CONNECTED     9559     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     10974    
unix  3      [ ]         STREAM     CONNECTED     7119     
unix  3      [ ]         STREAM     CONNECTED     9615     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     12374    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     12501    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     13386    
unix  3      [ ]         STREAM     CONNECTED     9211     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     1677     /run/systemd/journal/stdout
unix  3      [ ]         DGRAM      CONNECTED     1412     /run/systemd/notify
unix  3      [ ]         STREAM     CONNECTED     9683     
unix  3      [ ]         STREAM     CONNECTED     14737    
unix  3      [ ]         STREAM     CONNECTED     7100     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     13381    
unix  3      [ ]         STREAM     CONNECTED     5697     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     8566     
unix  3      [ ]         STREAM     CONNECTED     12911    
unix  3      [ ]         STREAM     CONNECTED     11909    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     9701     
unix  3      [ ]         STREAM     CONNECTED     12418    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     8671     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     12294    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     8513     
unix  3      [ ]         STREAM     CONNECTED     11926    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12405    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     11452    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     7113     
unix  3      [ ]         STREAM     CONNECTED     11460    @/tmp/.ICE-unix/1182
unix  3      [ ]         STREAM     CONNECTED     6595     
unix  3      [ ]         STREAM     CONNECTED     10091    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9702     
unix  13     [ ]         DGRAM      CONNECTED     1435     /run/systemd/journal/dev-log
unix  6      [ ]         DGRAM      CONNECTED     1436     /run/systemd/journal/socket
unix  3      [ ]         STREAM     CONNECTED     7118     
unix  3      [ ]         STREAM     CONNECTED     12378    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     6566     
unix  3      [ ]         STREAM     CONNECTED     11923    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9558     
unix  3      [ ]         STREAM     CONNECTED     10084    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     6121     
unix  3      [ ]         STREAM     CONNECTED     5745     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     7135     
unix  3      [ ]         STREAM     CONNECTED     12940    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     9685     
unix  3      [ ]         STREAM     CONNECTED     9729     @/tmp/.ICE-unix/1182
unix  3      [ ]         STREAM     CONNECTED     13380    
unix  3      [ ]         STREAM     CONNECTED     10085    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9318     
unix  2      [ ]         DGRAM      CONNECTED     6567     
unix  3      [ ]         STREAM     CONNECTED     14475    
unix  3      [ ]         STREAM     CONNECTED     10426    
unix  3      [ ]         STREAM     CONNECTED     11547    
unix  3      [ ]         STREAM     CONNECTED     12399    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     8629     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     107632   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     8569     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     7164     
unix  3      [ ]         STREAM     CONNECTED     10493    
unix  3      [ ]         STREAM     CONNECTED     13493    @/tmp/.ICE-unix/1182
unix  3      [ ]         STREAM     CONNECTED     7060     
unix  3      [ ]         STREAM     CONNECTED     76293    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     11466    
unix  3      [ ]         STREAM     CONNECTED     10702    
unix  3      [ ]         STREAM     CONNECTED     13472    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     10479    
unix  2      [ ]         DGRAM      CONNECTED     1778     
unix  3      [ ]         STREAM     CONNECTED     14461    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     7099     
unix  3      [ ]         STREAM     CONNECTED     11386    
unix  3      [ ]         STREAM     CONNECTED     11459    
unix  3      [ ]         STREAM     CONNECTED     7163     
unix  3      [ ]         STREAM     CONNECTED     10092    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     11577    
unix  3      [ ]         STREAM     CONNECTED     7059     
unix  3      [ ]         STREAM     CONNECTED     9215     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     9496     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     8051     
unix  3      [ ]         STREAM     CONNECTED     99318    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     11413    
unix  3      [ ]         STREAM     CONNECTED     10668    
unix  3      [ ]         STREAM     CONNECTED     9635     /run/user/1000/bus
unix  2      [ ]         DGRAM      CONNECTED     1756     
unix  3      [ ]         STREAM     CONNECTED     9574     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     106659   
unix  2      [ ]         DGRAM                    14422    
unix  3      [ ]         STREAM     CONNECTED     5763     @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     10686    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     11581    
unix  3      [ ]         STREAM     CONNECTED     7098     
unix  3      [ ]         STREAM     CONNECTED     9207     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     106663   
unix  3      [ ]         STREAM     CONNECTED     12433    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     10599    
unix  3      [ ]         STREAM     CONNECTED     11599    
unix  3      [ ]         STREAM     CONNECTED     11553    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     106660   
unix  3      [ ]         STREAM     CONNECTED     12440    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     1830     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     6600     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     10675    
unix  3      [ ]         STREAM     CONNECTED     12340    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     11570    
unix  3      [ ]         STREAM     CONNECTED     9807     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     7001     @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     78220    
unix  3      [ ]         STREAM     CONNECTED     11465    
unix  3      [ ]         STREAM     CONNECTED     11387    
unix  3      [ ]         STREAM     CONNECTED     10653    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12338    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     9814     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     10594    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     13320    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     8043     
unix  3      [ ]         STREAM     CONNECTED     11470    
unix  3      [ ]         STREAM     CONNECTED     9582     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     10976    
unix  3      [ ]         STREAM     CONNECTED     7146     
unix  3      [ ]         STREAM     CONNECTED     12384    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     11585    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     11569    
unix  3      [ ]         STREAM     CONNECTED     12403    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     1770     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     77250    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     14451    
unix  3      [ ]         STREAM     CONNECTED     10627    
unix  3      [ ]         STREAM     CONNECTED     10425    
unix  3      [ ]         STREAM     CONNECTED     11576    
unix  3      [ ]         STREAM     CONNECTED     7061     
unix  3      [ ]         STREAM     CONNECTED     78219    
unix  3      [ ]         STREAM     CONNECTED     13398    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     1828     
unix  3      [ ]         STREAM     CONNECTED     10979    
unix  3      [ ]         STREAM     CONNECTED     7153     
unix  3      [ ]         STREAM     CONNECTED     11942    
unix  3      [ ]         STREAM     CONNECTED     14480    /run/user/1000/gvfsd/socket-59x9vaLJ
unix  3      [ ]         STREAM     CONNECTED     7055     
unix  3      [ ]         STREAM     CONNECTED     102154   
unix  3      [ ]         STREAM     CONNECTED     11463    
unix  3      [ ]         STREAM     CONNECTED     1792     
unix  3      [ ]         STREAM     CONNECTED     14419    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     11924    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12519    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     7096     
unix  3      [ ]         STREAM     CONNECTED     106662   
unix  3      [ ]         STREAM     CONNECTED     11388    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     11469    
unix  3      [ ]         STREAM     CONNECTED     14460    
unix  3      [ ]         STREAM     CONNECTED     11600    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     9727     /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     12359    
unix  2      [ ]         DGRAM      CONNECTED     1791     
unix  3      [ ]         DGRAM      CONNECTED     7640     
unix  3      [ ]         STREAM     CONNECTED     7091     /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     104970   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     10977    
unix  3      [ ]         STREAM     CONNECTED     9633     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     12550    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     6133     @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     104969   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     1789     
unix  3      [ ]         STREAM     CONNECTED     10636    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     14339    
unix  3      [ ]         STREAM     CONNECTED     12916    /run/user/1000/at-spi/bus_0
unix  3      [ ]         STREAM     CONNECTED     11582    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     5679     /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     104015   /run/user/1000/at-spi/bus_0
unix  2      [ ]         STREAM                   11571    @printer-applet-lock-user-nightweaver01
unix  3      [ ]         STREAM     CONNECTED     6079     @4a43a0fab785cdef/bus/systemd/bus-api-user
unix  3      [ ]         STREAM     CONNECTED     7697     @433b54ba74270992/bus/systemd/bus-api-system
unix  3      [ ]         STREAM     CONNECTED     6013     @3f33be25db0ecd45/bus/systemd/bus-system
unix  3      [ ]         STREAM     CONNECTED     1767     @475d2b7f5f9a4f4e/bus/systemd-logind/system
Connection Test:
I established a local connection to the port.
code
Bash
nc 127.0.0.1 4444
Result: The message "Hello Hacker" was successfully received on the listener terminal.
