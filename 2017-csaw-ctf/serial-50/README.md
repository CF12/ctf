# Serial
Miscellaneous - 50 - Unknown Solve Count ¯\\\_(ツ)\_/¯
> nc misc.chal.csaw.io 4239

## Writeup
In this challenge, we're presented with a netcat command to a server. When you connect to the server, you receive the following response:
```
8-1-1 even parity. Respond with '1' if you got the byte, '0' to retransmit.
[11 bit binary sequence that varies every time. Ex. 01101011011]
```

When you respond with a 1, the server returns with another 11 bit piece of data. When you respond with a 0, the server seemlingly sends another piece of data. The data changes between sessions as well. Seems a bit wacky, right?

We decided to perform a bit of research on serial. It turned out that serial, in the case of this challenge, was referring to Serial Ports. Serial Ports have a conventional syntax and format for the bits of data it sends. The syntax is explained as data/parity/stop (D/P/S). In our scenario, 8-1-1 was our syntax, whereas:
- **8** referred to **8** bits of data.
- **1** referred to **1** parity bit.
- **1** referred to **1** stop bit. (Always 1)
- The "even parity" phrase refers to an even parity bit, which ensures that the number of '1's in the data bytes are always an even amount.
- The sequences of bits all contained a "start bit" (which was always 0)

The server then proceeds to send us a total of **90** serial bytes. We decided to write a python script to decode the data byte of the serial byte to ASCII:

```
34;}`/55>9;32q3o:z;Y7.rp22'22;>?06/(*t:33>+06'3 8$o3$!;$::1>70z5#. x:x267>6E
```

Hmm... That doesn't seem quite right... We looked over the results, and we found that the server was sending numerous **invalid** parities. For example, we received a byte where the number of '1's within the 9 data bits + parity bit wasn't an even number. Therefore, we altered our python script to check the validity of the parity bit, and tweaked it so that the script would request another byte (send a '0' as a response) until it found a valid byte. We ended up with a result of **89** valid bytes of data, which we then converted over to ASCII to receive the flag.

You can view the full solution in [solve.py](./solve.py)

## Flag
```
flag{@n_int3rface_betw33n_data_term1nal_3quipment_and_d@t@_circuit-term1nating_3quipment}
```

## Closing
Thanks for reading! If you notice any errors, or if you have any suggestions, please feel free to submit a GitHub issue and / or a PR to the repo. Happy hacking!

## References
- https://en.wikipedia.org/wiki/8-N-1
- https://en.wikipedia.org/wiki/Serial_port

## Other writeups
- https://noobsinthehood.gitbooks.io/nith/content/misc-50-serial.html
