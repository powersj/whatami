package filesystem

import (
	"whatsthis/pkg/file"
)

// Etc represents the /etc filesystem
type Etc struct{}

// OSRelease read from /etc/os-release
func (*Etc) OSRelease() map[string]string {
	return file.ParseKeyValue("/etc/os-release", "=")
}
