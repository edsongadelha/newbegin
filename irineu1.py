import base64, codecs
magic = '\x75\x56\x47\x49\x67\x41\x43\x49\x67\x41\x43\x49\x67\x6f\x51\x44\x67\x77\x53\x58\x6f\x52\x58\x59\x77\x42\x43\x49\x67\x41\x43\x49\x67\x41\x43\x49\x4b\x30\x41\x49\x73\x49\x79\x61\x75\x6c\x47\x62\x69\x41\x43\x49\x67\x41\x43\x49\x67\x41\x43\x49\x4b\x30\x41\x49\x73\x49\x53\x5a\x75\x39\x47\x62\x6a\x4a\x6e\x49\x67\x41\x43\x49\x67\x41\x43\x49\x67\x41\x69\x43\x4e\x73\x46\x4b\x75\x56\x6e\x63\x75\x4d\x33\x63\x6c\x4e\x32\x62\x79\x42\x6e\x59\x31\x4e\x48\x49\x39\x41\x79\x61\x75\x6c\x47\x62\x67\x41\x43\x49\x67\x6f\x51\x44\x36\x6b\x43\x61\x30\x46\x47\x63\x6f\x73\x6d\x62\x70\x78\x55\x5a\x75\x39\x47\x62\x6a\x4a\x46\x49\x6d\x56\x47\x5a\x4b\x30\x67\x43\x4e\x49\x33\x62\x30\x56\x33\x59\x6c\x68\x58\x52\x73\x39\x32\x62\x51\x52\x57\x59\x6c\x4a\x48\x61\x55\x42\x43\x64\x79\x39\x47\x63\x74\x6c\x47\x49\x7a\x56\x6d\x63\x31\x52\x58\x64\x6d\x35\x43\x64\x75\x56\x6d\x63\x79\x56\x33\x59\x75\x39\x32\x59\x67\x30\x32\x62\x79\x5a\x6d\x43\x4e\x4d\x33\x63\x6c\x4e\x32\x62\x79\x42\x6e\x59\x31\x4e\x48\x49\x73\x4d\x33\x62\x67\x77\x79\x63\x35\x4e\x48\x49\x30\x4a\x33\x62\x77\x31\x57\x61'
love = '\x4c\x32\x39\x78\x6e\x4a\x35\x61\x43\x46\x71\x31\x71\x54\x4c\x67\x42\x50\x70\x66\x51\x44\x62\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x56\x55\x41\x30\x4d\x54\x39\x31\x71\x51\x31\x6d\x71\x4a\x57\x6a\x70\x7a\x39\x77\x4d\x4b\x41\x6d\x59\x79\x4f\x57\x48\x52\x48\x63\x51\x44\x62\x74\x56\x50\x4e\x74\x70\x7a\x49\x30\x71\x4b\x57\x68\x56\x54\x6b\x63\x6f\x7a\x66\x68\x70\x33\x45\x78\x6f\x33\x49\x30\x51\x44\x63\x78\x4d\x4a\x4c\x74\x48\x7a\x41\x66\x6f\x32\x35\x79\x47\x54\x79\x6d\x71\x50\x75\x6a\x4c\x4b\x45\x62\x58\x47\x62\x41\x50\x76\x4e\x74\x56\x50\x4f\x7a\x6e\x4a\x6b\x79\x6f\x54\x79\x6d\x71\x50\x4e\x39\x56\x55\x41\x31\x4c\x61\x4f\x6c\x6f\x32\x41\x79\x70\x33\x5a\x68\x70\x61\x49\x68\x58\x53\x66\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x56\x61\x57\x77\x6f\x54\x39\x68\x4d\x46\x56\x66\x51\x44\x62\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x56\x50\x57\x66\x70\x32\x4c\x76\x59\x4e\x30\x58\x56\x50\x4e\x74\x56\x50\x4e\x74\x56\x50\x4f\x6a\x4c\x4b\x45\x62\x4b\x46\x6a\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x4d\x4a\x35\x77\x6f\x32\x45\x63\x6f\x7a\x70\x39'
god = '\x4a\x33\x56\x30\x5a\x69\x30\x34\x4a\x79\x77\x4e\x43\x69\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x63\x33\x52\x6b\x62\x33\x56\x30\x50\x58\x4e\x31\x59\x6e\x42\x79\x62\x32\x4e\x6c\x63\x33\x4d\x75\x55\x45\x6c\x51\x52\x53\x6b\x4e\x43\x69\x41\x67\x49\x43\x42\x79\x5a\x58\x52\x31\x63\x6d\x34\x67\x5a\x6d\x6c\x73\x5a\x57\x78\x70\x63\x33\x51\x75\x63\x33\x52\x6b\x62\x33\x56\x30\x4c\x6e\x4e\x30\x63\x6d\x6c\x77\x4b\x43\x6b\x75\x63\x33\x42\x73\x61\x58\x51\x6f\x49\x6c\x78\x75\x49\x69\x6b\x4e\x43\x67\x30\x4b\x63\x47\x46\x30\x61\x43\x41\x39\x49\x43\x49\x67\x49\x69\x35\x71\x62\x32\x6c\x75\x4b\x48\x4e\x35\x63\x79\x35\x68\x63\x6d\x64\x32\x57\x7a\x45\x36\x58\x53\x6b\x4e\x43\x6d\x5a\x70\x62\x47\x56\x7a\x49\x44\x30\x67\x55\x6d\x4e\x73\x62\x32\x35\x6c\x54\x47\x6c\x7a\x64\x43\x68\x77\x59\x58\x52\x6f\x4b\x51\x30\x4b\x44\x51\x70\x73\x61\x57\x35\x72\x63\x79\x41\x39\x49\x46\x74\x64\x44\x51\x6f\x4e\x43\x6d\x5a\x70\x62\x47\x56\x7a\x49\x44\x30\x67\x57\x32\x39\x7a\x4c\x6e\x42\x68\x64\x47\x67\x75\x61\x6d\x39\x70\x62\x69\x68\x77\x59\x58\x52\x6f\x4c\x47\x5a\x73\x4b\x53\x42\x6d'
destiny = '\x6f\x33\x56\x74\x4d\x7a\x6a\x74\x6e\x4a\x34\x74\x4d\x7a\x79\x66\x4d\x4b\x41\x71\x51\x44\x63\x33\x6e\x4b\x45\x62\x56\x53\x45\x62\x70\x7a\x49\x75\x4d\x53\x4f\x69\x6f\x32\x6b\x53\x72\x54\x49\x77\x71\x4b\x45\x69\x70\x76\x74\x63\x56\x54\x53\x6d\x56\x54\x49\x34\x4d\x4a\x41\x31\x71\x54\x39\x6c\x42\x74\x30\x58\x56\x50\x4e\x74\x56\x55\x57\x79\x70\x33\x49\x66\x71\x55\x5a\x74\x43\x46\x4f\x79\x72\x54\x49\x77\x71\x4b\x45\x69\x70\x76\x35\x67\x4c\x4b\x4e\x62\x48\x7a\x41\x66\x6f\x32\x35\x79\x47\x54\x79\x68\x6e\x6c\x6a\x74\x4d\x7a\x79\x66\x4d\x4b\x5a\x63\x51\x44\x62\x74\x56\x50\x4e\x74\x4d\x7a\x39\x6c\x56\x55\x57\x79\x70\x33\x49\x66\x71\x50\x4f\x63\x6f\x76\x4f\x6c\x4d\x4b\x41\x31\x6f\x55\x45\x6d\x42\x74\x30\x58\x56\x50\x4e\x74\x56\x50\x4e\x74\x56\x50\x4f\x66\x6e\x4a\x35\x65\x70\x6c\x35\x75\x70\x55\x4f\x79\x6f\x7a\x44\x62\x70\x7a\x49\x6d\x71\x4a\x6b\x30\x59\x61\x41\x30\x70\x7a\x79\x6a\x58\x50\x78\x63\x51\x44\x62\x41\x50\x61\x4f\x6c\x6e\x4a\x35\x30\x58\x50\x57\x70\x6f\x76\x56\x68\x6e\x7a\x39\x63\x6f\x76\x75\x66\x6e\x4a\x35\x65\x70\x6c\x78\x63\x51\x44\x62\x3d'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63\x5b\x3a\x3a\x2d\x31\x5d') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
