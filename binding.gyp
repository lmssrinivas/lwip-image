{
    "targets": [{
        "target_name": "lwip_image",
        "sources": [
            # LWIP:
            #######
            "src/image/init.cpp",
            "src/image/image.cpp",
            "src/image/resize_worker.cpp",
            "src/image/rotate_worker.cpp",
            "src/image/blur_worker.cpp",
            "src/image/crop_worker.cpp",
            "src/image/mirror_worker.cpp",
            "src/image/pad_worker.cpp",
            "src/image/sharpen_worker.cpp",
            "src/image/hsla_worker.cpp",
            "src/image/opacify_worker.cpp",
            "src/image/paste_worker.cpp",
            "src/image/setpixel_worker.cpp",
        ],
        'include_dirs': [
            '<!(node -e "require(\'nan\')")',
            'src/lib/cimg',
        ],
        'conditions': [
            ['OS=="freebsd"', {
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
            }],
            ['OS=="solaris"', {
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
            }],
            ['OS=="linux"', {
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
            }],
            ['OS=="mac"', {
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                },
                'include_dirs': ['/usr/include/malloc']
            }],
            ['OS=="win"', {
                'configurations': {
                    'Release': {
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'ExceptionHandling': 1
                            }
                        }
                    }
                }
            }]
        ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }]
}
