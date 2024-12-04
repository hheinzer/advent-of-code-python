const std = @import("std");

pub fn main() !void {
    const allocator = std.heap.page_allocator;

    const file = try std.fs.cwd().openFile("input/01.txt", .{});
    defer file.close();

    var left = std.ArrayList(i32).init(allocator);
    defer left.deinit();

    var right = std.ArrayList(i32).init(allocator);
    defer right.deinit();

    var buffer: [256]u8 = undefined;
    while (try file.reader().readUntilDelimiterOrEof(&buffer, '\n')) |line| {
        var token = std.mem.tokenizeScalar(u8, line, ' ');
        try left.append(try std.fmt.parseInt(i32, token.next() orelse unreachable, 10));
        try right.append(try std.fmt.parseInt(i32, token.next() orelse unreachable, 10));
    }

    std.mem.sort(i32, left.items, {}, comptime std.sort.asc(i32));
    std.mem.sort(i32, right.items, {}, comptime std.sort.asc(i32));

    var part_one: i32 = 0;
    for (left.items, right.items) |a, b| {
        part_one += @max(a, b) - @min(a, b);
    }
    std.debug.print("{d}\n", .{part_one});

    var part_two: i32 = 0;
    for (left.items) |a| {
        var count: i32 = 0;
        for (right.items) |b| {
            count += if (a == b) 1 else 0;
        }
        part_two += a * count;
    }
    std.debug.print("{d}\n", .{part_two});
}
